from batch_4.session_5 import CompanyInfo
from batch_4.session_5.three_database import DBConnection


class Utility:

    def mapper(self, fileName):
        companyInfos = []

        sg_data_file = open(fileName, "r")
        data = sg_data_file.read()
        comp_list = data.splitlines()
        for company in comp_list:
            columns = Utility.separator(company,",")
            # create object oif Company Info
            company = CompanyInfo(columns[0], columns[1], columns[2], columns[3], columns[4])
            # append that object to list.
            companyInfos.append(company)
        sg_data_file.close()

        return companyInfos

    def mapperWithBuffer(self, fileName):
        companyInfos = []

        sg_data_file = open(fileName, "r")
        bufferSize = 200
        data = sg_data_file.read(bufferSize)
        while len(data):
            comp_list = data.splitlines()
            for company in comp_list:
                columns = Utility.separator(company,",")
                if len(columns) >= 5:
                    # create object oif Company Info
                    company = CompanyInfo(columns[0], columns[1], columns[2], columns[3], columns[4])
                    # append that object to list.
                    companyInfos.append(company)
            data = sg_data_file.read(bufferSize)
        sg_data_file.close()

        return companyInfos

    @staticmethod
    def separator(data, separator):
        return data.split(separator)


    def start(self):
            # compDataList = self.mapperWithBuffer("data.csv")
            # db = DBConnection()
            # for comp in compDataList:
            #
            #     print(comp.compId +  " -- " + comp.compName)
            #     # db.insert_company(comp)

            db = DBConnection()
            compDataList = db.select_company()
            for comp in compDataList:
                print(str(comp.compId) +  " -- " + str(comp.compName))





if __name__ == "__main__":

    utility = Utility()
    utility.start()