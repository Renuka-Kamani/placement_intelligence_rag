
import pandas as pd


class KnowledgeService:

    @staticmethod
    def load_company_data():

        data = {

            "Company": [
                "TCS",
                "Infosys",
                "Deloitte",
                "Accenture",
                "Amazon",
                "Flipkart",
                "Google",
                "Microsoft",
                "Wipro",
                "Cognizant",
                "Capgemini",
                "IBM",
                "Adobe",
                "Oracle",
                "SAP",
                "HCL",
                "Tech Mahindra",
                "Qualcomm",
                "Intel",
                "Samsung R&D"
            ],

            "CGPA": [
                7.5,
                8.0,
                7.7,
                8.2,
                6.4,
                7.8,
                7.4,
                6.1,
                6.7,
                8.4,
                7.1,
                7.5,
                7.5,
                7.7,
                8.4,
                8.4,
                8.1,
                7.2,
                7.0,
                6.3
            ],

            "Backlogs": [
                0,
                0,
                1,
                0,
                1,
                2,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0
            ],

            "Package": [
                4.1,
                42.9,
                9.6,
                17.3,
                28.6,
                25.3,
                42.0,
                21.0,
                22.2,
                34.2,
                29.1,
                18.4,
                15.2,
                13.8,
                17.5,
                21.3,
                28.7,
                33.2,
                32.5,
                6.4
            ],

            "Bond": [
                0,
                0,
                1,
                2,
                2,
                2,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],

            "Focus": [
                "System Design",
                "Java",
                "System Design",
                "Cloud",
                "C++",
                "Python",
                "Python",
                "C++",
                "Java",
                "Java",
                "Cloud",
                "DBMS",
                "Algorithms",
                "Database",
                "SAP",
                "Networking",
                "Java",
                "Embedded Systems",
                "C++",
                "Hardware"
            ]
        }

        return pd.DataFrame(data)
