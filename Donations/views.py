from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import Donations
from .forms import Donations_Form
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


def donates_form(request):
    if request.method == 'GET':
        return render(request, 'Donations/index.html', {'form': Donations_Form()})
    else:
        form = Donations_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            id_number = form.cleaned_data.get("id_number")
            credit_number = form.cleaned_data.get("credit_number")
            cvc = form.cleaned_data.get("cvc")
            amount = form.cleaned_data.get("amount")

            obj = Donations.objects.create(
                name=name,
                id_number=id_number,
                credit_number=credit_number,
                cvc=cvc,
                amount=amount,
            )
            obj.save()
        else:
            print(form.errors)  # in case of errors in validation
        return redirect('Donations:Thankyou')


def Thankyou(request):
    return render(request, 'Donations/Thankyou.html', {})


def submit(request):
    name = request.POST['name']
    credit = request.POST['credit']
    donates = Donations(name=name, credit=credit)
    donates.save()
    Donors = Donations.objects.all()
    return render(request, 'Donations/index.html', {'Donors': Donors})


def all_Donors(request):
    Donors = Donations.objects.all()
    if not Donors:
        Donors = {}
    return render(request, 'Donations/index.html', {'Donors': Donors})


def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('Tahoma', 'Tahoma.ttf'))
    textob.setFont("Tahoma", 14)  # set the font of the text

    donations = Donations.objects.all()  # designate the model
    lines = []  # creat a new list for the objects

    sum = 0  # accumulation variable for calculating the total amount of donations
    for donation in donations:
        sum += int(donation.amount)

    # print all data we need
    for donation in donations:
        lines.append('Donor name: ' + donation.name)
        lines.append('Donor ID: ' + donation.id_number)
        lines.append('Amount: ' + donation.amount + '₪')
        lines.append('    ')
        lines.append('----------------------------------')
        lines.append('    ')

    lines.append('Total:' + str(sum) + '₪')

    textob.textLine("Revenue report of the 'Bait Ham' association:")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='donations.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='donations/excel')
    response['Content-Disposition'] = 'attachment; filename=donations' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('donations')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Revenue report of the "Bait Ham" association:', font_style)  # the title of the file

    columns = ['Name', 'ID Number', 'Amount']  # the columns in the table
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = Donations.objects.all().values_list('name', 'id_number', 'amount')

    font_style = xlwt.XFStyle()

    donations = Donations.objects.all()
    sum = 0
    # calculate the total amount from donations
    for donation in donations:
        sum += int(donation.amount)

    count = 0
    # calculate the number of rows in the table for the objects
    for donation in donations:
        count += 1

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ws.write(count + 3, 1, 'Total:', font_style)
    ws.write(count + 3, 2, str(sum) + '₪', font_style)  # print the total amount

    wb.save(response)  # save the file

    return response
