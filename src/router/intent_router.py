class IntentRouter:

    @staticmethod
    def detect_intent(
        question: str
    ) -> str:

        q = question.lower()

        structured_keywords = [

            "package",
            "cgpa",
            "eligibility",
            "criteria",
            "backlog",
            "compare",
            "highest",
            "lowest",
            "top",
            "bond",
            "salary"

        ]

        web_keywords = [

            "ceo",
            "stock",
            "founder",
            "current",
            "latest",
            "today"

        ]

        rag_keywords = [

            "round",
            "interview",
            "conduct",
            "process"

        ]

        for keyword in web_keywords:

            if keyword in q:

                return "web"

        for keyword in structured_keywords:

            if keyword in q:

                return "mysql"

        for keyword in rag_keywords:

            if keyword in q:

                return "rag"

        return "rag"