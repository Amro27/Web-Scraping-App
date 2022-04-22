# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: frmRegistration.py
from MyLib import *
from UiRegistration import Ui_frm_Registration as UiRegistration_Ui

class Create(QDialog, UiRegistration_Ui):

    def closeEvent(self, *args, **kwargs):
        self.timer.stop

    def __init__(self, parent=None):
        super(Create, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setFixedSize(371, 131)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.f = self.parent
        self.btn_Registration = self.findChild(QPushButton, 'btn_Registration')
        self.btn_Registration.clicked.connect(self.btn_click)
        self.btn_SendOTP = self.findChild(QPushButton, 'btn_SendOTP')
        self.btn_SendOTP.clicked.connect(self.btn_click)
        self.OTP = None
        self.txt_OTP = self.findChild(QLineEdit, 'txt_OTP')
        self.txt_OTP.textChanged.connect(self.text_changed)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(200)

    def update_ui(self):

        def sec2time(sec, n_msec=3):
            """ Convert seconds to 'D days, HH:MM:SS.FFF' """
            if hasattr(sec, '__len__'):
                return [sec2time(s) for s in sec]
            else:
                m, s = divmod(sec, 60)
                h, m = divmod(m, 60)
                d, h = divmod(h, 24)
                if n_msec > 0:
                    pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec + 3, n_msec)
                else:
                    pattern = '%02d:%02d:%02d'
            if d == 0:
                return pattern % (h, m, s)
            return ('%d days, ' + pattern) % (d, h, m, s)

        A = self.f.Last_OTP_Sent
        i = 1
        if A != None:
            sec = (datetime.now() - A).total_seconds()
            if sec <= 299:
                self.btn_SendOTP.setEnabled(False)
                _ = sec2time(300 - sec, 0)
                self.setWindowTitle('Web Scraping Registration - {} '.format(_[3:]))
        else:
            self.btn_SendOTP.setEnabled(True)
            self.setWindowTitle('Web Scraping Registration')

    def send_OTP(self):
        SMTPserver = 'smtp.gmail.com'
        sender = 'elmatator.itachi@gmail.com'
        destination = 'elmatator.itachi@gmail.com'
        USERNAME = 'elmatator.itachi@gmail.com'
        PASSWORD = '@mrMohamed27'
        text_subtype = 'plain'
        self.OTP = f"{random.randrange(1, 10000):04}"
        content = '      {}\n      '.format(self.OTP)
        subject = 'Web Scraping OTP'
        try:
            msg = MIMEText(content, text_subtype)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = destination
            conn = SMTP(SMTPserver)
            conn.set_debuglevel(False)
            conn.login(USERNAME, PASSWORD)
            try:
                conn.sendmail(sender, msg['To'], msg.as_string())
                self.f.Count_OTP_Sent += 1
                self.f.Last_OTP_Sent = datetime.now()
                self.f.cur.execute("UPDATE registration SET `Last OTP Sent`='{}', `Count OTP Sent`='{}' WHERE registration.`Key` = '{}';".format(self.f.Last_OTP_Sent, self.f.Count_OTP_Sent, self.f.Key))
                self.f.con.commit()
            finally:
                conn.quit()

        except:
            import traceback
            print(traceback.format_exc())
            sys.exit('mail failed; %s' % 'CUSTOM_ERROR')

    def btn_click(self):
        sender = self.sender()
        if sender.objectName() == 'btn_Registration':
            if self.f.Last_OTP_Sent == '':
                sec = (datetime.now() - self.f.Last_OTP_Sent).total_seconds()
            else:
                sec = 0
            if self.txt_OTP.text() == self.OTP and sec <= 300:
                show_pop('Registration', 'Registered Successfully', QMessageBox.Information)
                self.f.cur.execute("UPDATE registration SET `Registered`='1' WHERE registration.`Key` = '{}';".format(self.f.Key))
                self.f.con.commit()
                self.close()
                self.done(2)
            elif self.txt_OTP.text() == self.OTP and sec > 300:
                show_pop('Error', 'OTP period expired', QMessageBox.Critical)
            elif self.txt_OTP.text() != self.OTP:
                show_pop('Incorrect OTP', 'The OTP you entered is incorrect.Please try again.', QMessageBox.Critical)
        elif sender.objectName() == 'btn_SendOTP':
            self.send_OTP()

    def text_changed(self):
        sender = self.sender()
        if sender.objectName() == 'txt_OTP':
            if len(self.txt_OTP.text()) == 0:
                self.btn_Registration.setEnabled(False)
            else:
                self.btn_Registration.setEnabled(True)