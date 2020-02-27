import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(emailAddress, password, content):
    port = 465
    smtpServer = "smtp.gmail.com"

    server = smtplib.SMTP_SSL(smtpServer, port)
    server.login(emailAddress, password)

    message = createEmail(emailAddress, content)

    server.sendmail(emailAddress, emailAddress, message.as_string())
    server.quit()

def createEmail(emailAddress, content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Canyon outlet update"
    msg['From'] = emailAddress
    msg['To'] = emailAddress

    text = createTxtMessage(content)
    html = """\
        <html>
        <head></head>
        <body>
            <table>
                <tr>
                    <td>Model</td>
                    <td>Price</td>
                    <td>Disc.</td>
                </tr>
        """

    for bike in content:
        html += '  <tr><td>'
        html += '    </td><td>'.join(bike)
        html += '  </td></tr>'

    html += """\
        </table>
        </body>
        </html>
        """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    return msg

def createTxtMessage(content):
    message = '%-*s %-*s %s\n\n' % (43, 'Model', 9, 'Price', 'Disc.')
    for element in content:
        message += '%-*s %-*s %s\n' % (40, element[0], 14, element[1], element[2])
    print(message)
    return message