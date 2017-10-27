# -*- coding: utf-8 -*-
import sys
import platform
import os



import pytest
#global path


from fixture.regHelperPersonal import regHelperPersonal
from fixture.regHelperEducation import regHelperEducation
from fixture.regHelperProfession import regHelperProfession
from fixture.regHelperAddInformation import regHelperAddinform
from fixture.regHelperMail_verify import regHelperMail
from fixture.regHelperBillInfo import regHelperBillInfo
from fixture.regHelpLogin_logout import regHelpLogin_out
from fixture.regHelperDB import regHelperDB
import conftest

#path = conftest.path
#sys.path.append(path)
#sys.path.append(path + "\Page")



@pytest.mark.usefixtures('start')
class Test_registration:



    def test_registration_login_password(self):

        regHelperPersonal.setup_registration(self)
        regHelperPersonal.switch_to_english(self)
        regHelperPersonal.go_registration(self)
        regHelperPersonal.email_name_login(self)
        regHelperPersonal.password_name_login(self)
        regHelperPersonal.submit_email_password(self)
        assert True
        print("Adding login and password was submit")

    def test_registration_contract(self):

        regHelperPersonal.submit_registration_contract(self)
        assert True
        print("Contract was submit")

    def test_registration_login_personal_data(self):

        regHelperPersonal.firstname(self)
        regHelperPersonal.lastname(self)
        regHelperPersonal.gender_select(self)
        regHelperPersonal.country(self)
        regHelperPersonal.country_field(self)
        regHelperPersonal.country_field_name(self)
        regHelperPersonal.city_field_name(self)
        regHelperPersonal.phone_id_select(self)
        regHelperPersonal.details_avatar(self)
        regHelperPersonal.check_personal_data(self)
        regHelperPersonal.details_submit(self)
        assert True
        print("Adding personal data was submit")


    def test_registration_education(self):

        regHelperEducation.select_school(self)
        regHelperEducation.select_school_country(self)
        regHelperEducation.city_field(self)
        regHelperEducation.city_select(self)
        regHelperEducation.year_select(self)
        regHelperEducation.university_select(self)
        regHelperEducation.specialization_select(self)
        regHelperEducation.diplom_select(self)
        regHelperEducation.select_qual_categor(self)
        regHelperEducation.select_qualification(self)
        regHelperEducation.select_academic_degree(self)
        regHelperEducation.select_academdegree(self)
        regHelperEducation.check_education_data(self)
        regHelperEducation.education_submit(self)
        assert True
        print("Adding education was submit")

    def test_registration_profession_experience(self):

        regHelperProfession.select_institution(self)
        regHelperProfession.select_country(self)
        regHelperProfession.city_field(self)
        regHelperProfession.city_select(self)
        regHelperProfession.year_select(self)
        regHelperProfession.institution_select(self)
        regHelperProfession.speciality_select(self)
        regHelperProfession.select_specialization(self)
        regHelperProfession.select_position(self)
        regHelperProfession.check_profession_data(self)
        regHelperProfession.profession_submit(self)
        assert True
        print("Adding profession experience was submit")

    def test_additional_information(self):

        regHelperAddinform.add_information(self)
        regHelperAddinform.check_additional_data(self)
        regHelperAddinform.submit_add(self)
        assert True
        print("Adding additional information was submit")

    def test_billing_information_and_final_submit(self):

        regHelperBillInfo.bill_information(self)
        regHelperBillInfo.check_bill(self)
        regHelperBillInfo.submit_bill(self)
        assert True
        print("Adding billing and final submit")

    def test_final_registration_submit(self):
        regHelperBillInfo.submit_registration(self)
        regHelpLogin_out.check_login(self)
        regHelpLogin_out.check_logout(self)
        assert True
        print("Logout after final submit is verified")


    def test_login(self):

        regHelpLogin_out.setup_login(self)
        regHelpLogin_out.switch_to_english(self)
        regHelpLogin_out.email_name_login(self)
        regHelpLogin_out.password_name_login(self)
        regHelpLogin_out.submit_login(self)
        regHelpLogin_out.check_login(self)
        regHelpLogin_out.check_logout(self)
        assert True
        print("Login and logout after final submit is verified")

    def test_delete_doctor_from_db(self):

        regHelperDB.setup_for_delete_doctor_in_db(self)
        regHelperDB.email_db_login(self)
        regHelperDB.password_name_login(self)
        regHelperDB.submit_db_login(self)
        regHelperDB.select_doctor_section(self)
        regHelperDB.delete_doctor_button(self)
        regHelperDB.verifying_delete_exit(self)
        assert True
        print("delete doctor in DB after registration is verified")

    def test_confirm__email_receive_end_delete(self):

        regHelperMail.test_setup(self)
        regHelperMail.login_mail(self)
        regHelperMail.select_email(self)
        regHelperMail.check_email(self)
        regHelperMail.mail_delete(self)
        regHelperMail.logout_email(self)
        assert True
        print("delete email after registration is verified")
    '''
    filename = path + "/Test_result/reg_log.txt"

    f = open(filename, "r+")
    print(f.read())
    f.truncate(0)
    f.close()
    '''





