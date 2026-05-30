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
                "Microsoft"
            ],

            "CGPA": [
                7.5,
                8.0,
                7.7,
                8.2,
                6.4,
                7.8,
                7.4,
                6.1
            ],

            "Backlogs": [
                0,
                0,
                1,
                0,
                1,
                2,
                0,
                1
            ],

            "Package": [
                4.1,
                42.9,
                9.6,
                17.3,
                28.6,
                25.3,
                42.0,
                21.0
            ],

            "Focus": [
                "System Design",
                "Java",
                "System Design",
                "Cloud",
                "C++",
                "Python",
                "Python",
                "C++"
            ]
        }

        return pd.DataFrame(
            data
        )