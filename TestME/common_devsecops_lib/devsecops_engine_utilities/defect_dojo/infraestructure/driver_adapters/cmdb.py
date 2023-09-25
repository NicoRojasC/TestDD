import json
from devsecops_engine_utilities.utils.api_error import ApiError
from devsecops_engine_utilities.utils.logger_info import MyLogger
from devsecops_engine_utilities.defect_dojo.domain.models.cmdb import Cmdb
from devsecops_engine_utilities.defect_dojo.infraestructure.driver_adapters.settings.settings import VERIFY_CERTIFICATE
from devsecops_engine_utilities.utils.session_manager import SessionManager
from devsecops_engine_utilities.settings import SETTING_LOGGER

logger = MyLogger.__call__(**SETTING_LOGGER).get_logger()


class CmdbRestConsumer:
    def __init__(self, token: str, host: str, mapping_cmdb: dict, session: SessionManager) -> None:
        self.__token = token
        self.__host = host
        self.__mapping_cmdb = mapping_cmdb
        self.__session = session

    def get_product_info(self, code_app: int) -> Cmdb:
        data = json.dumps({"codapp": code_app})
        headers = {"tokenkey": self.__token, "Content-Type": "application/json"}

        logger.info("Search info of name product")

        response = self.__session.post(self.__host, headers=headers, data=data, verify=VERIFY_CERTIFICATE)

        if response.status_code != 200:
            raise ApiError(response.json()["Message"])
        if response.json() == []:
            e = f"Engagement: {code_app} not found"
            logger.error(e)
            raise ApiError(e)
        data = response.json()[0]
        data_map = self.mapping_cmdb(data)
        logger.info(data_map)
        cmdb_object = Cmdb.from_dict(data_map)
        return cmdb_object

    def mapping_cmdb(self, data):
        data_map = {}
        for key, value in self.__mapping_cmdb.items():
            data_map[key] = data[value]
        return data_map
