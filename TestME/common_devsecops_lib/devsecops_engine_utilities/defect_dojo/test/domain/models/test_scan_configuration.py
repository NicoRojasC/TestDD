from devsecops_engine_utilities.defect_dojo.domain.models.scan_configuration import ScanConfigurationList


class TestScanConfigurationList:
    def test_init(self):
        scan_config_list = ScanConfigurationList()
        assert scan_config_list.count == 2
        assert scan_config_list.next is None
        assert scan_config_list.previous is None
        assert scan_config_list.results == []
