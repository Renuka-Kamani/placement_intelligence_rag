class CompanyDataService:

    COMPANY_DATA = {

        "tcs": {
            "cgpa": 7.5,
            "backlogs": 0,
            "package": 4.1,
            "focus": "System Design",
            "rounds": [
                "Online Assessment",
                "Technical Interview",
                "HR Interview"
            ]
        },

        "infosys": {
            "cgpa": 8.0,
            "backlogs": 0,
            "package": 42.9,
            "focus": "Java"
        },

        "deloitte": {
            "cgpa": 7.7,
            "backlogs": 1,
            "package": 9.6,
            "focus": "System Design"
        },

        "accenture": {
            "cgpa": 8.2,
            "backlogs": 0,
            "package": 17.3,
            "focus": "System Design"
        },

        "amazon": {
            "cgpa": 6.4,
            "backlogs": 1,
            "package": 28.6,
            "focus": "C++"
        },

        "flipkart": {
            "cgpa": 7.8,
            "backlogs": 2,
            "package": 25.3,
            "focus": "Python"
        },

        "google": {
            "cgpa": 7.4,
            "backlogs": 0,
            "package": 42.0,
            "focus": "Python"
        },

        "microsoft": {
            "cgpa": 6.1,
            "backlogs": 1,
            "package": 21.0,
            "focus": "C++"
        }

    }

    @staticmethod
    def answer(question):

        q = question.lower()

        for company in (
            CompanyDataService
            .COMPANY_DATA
        ):

            if company in q:

                data = (
                    CompanyDataService
                    .COMPANY_DATA[
                        company
                    ]
                )

                # Package
                if "package" in q:

                    return (
                        f"{company.title()} "
                        f"offers "
                        f"{data['package']} LPA."
                    )

                # Backlogs
                if (
                    "backlog" in q
                ):

                    if (
                        data[
                            "backlogs"
                        ] > 0
                    ):

                        return (
                            f"Yes, "
                            f"{company.title()} "
                            f"allows "
                            f"{data['backlogs']} "
                            f"backlog(s)."
                        )

                    return (
                        f"No, "
                        f"{company.title()} "
                        f"does not allow "
                        f"backlogs."
                    )

                # CGPA
                if (
                    "cgpa" in q
                ):

                    return (
                        f"{company.title()} "
                        f"requires "
                        f"{data['cgpa']} CGPA."
                    )

                # Rounds
                if (
                    "round" in q
                ):

                    if (
                        "rounds"
                        in data
                    ):

                        rounds = (
                            ", ".join(
                                data[
                                    "rounds"
                                ]
                            )
                        )

                        return (
                            f"{company.title()} "
                            f"conducts "
                            f"{len(data['rounds'])} "
                            f"rounds: "
                            f"{rounds}."
                        )

        return None