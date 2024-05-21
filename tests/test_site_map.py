from page_object.site_map import SiteMap


class TestSiteMap:

    def test_go_to_alert_status(self, browser):
        site_main_page = SiteMap(browser)
        site_main_page.go_to_site()
        site_main_page.go_to_alert_status()
        site_main_page.check_header()
        response_code = site_main_page.get_status_code()
        assert response_code == 200, f'Response code is {response_code}, should be 200'

    def test_go_to_about_the_air_district(self, browser):
        site_main_page = SiteMap(browser)
        site_main_page.go_to_site()
        site_main_page.go_to_about_the_air_district()
        site_main_page.check_header()
        response_code = site_main_page.get_status_code()
        assert response_code == 200, f'Response code is {response_code}, should be 200'

    def test_go_to_public_data_center(self, browser):
        site_main_page = SiteMap(browser)
        site_main_page.go_to_site()
        site_main_page.go_to_public_data_center()
        site_main_page.check_header()
        response_code = site_main_page.get_status_code()
        assert response_code == 200, f'Response code is {response_code}, should be 200'

    def test_go_to_online_services(self, browser):
        site_main_page = SiteMap(browser)
        site_main_page.go_to_site()
        site_main_page.go_to_online_services()
        site_main_page.check_header()
        response_code = site_main_page.get_status_code()
        assert response_code == 200, f'Response code is {response_code}, should be 200'

    def test_go_to_publications(self, browser):
        site_main_page = SiteMap(browser)
        site_main_page.go_to_site()
        site_main_page.go_to_publications()
        site_main_page.check_header()
        response_code = site_main_page.get_status_code()
        assert response_code == 200, f'Response code is {response_code}, should be 200'
