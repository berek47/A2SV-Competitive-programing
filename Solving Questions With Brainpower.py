class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        num_questions = len(questions)
        dp = [0] * (num_questions + 1)

        for i in range(num_questions - 1, -1, -1):
            points, brainpower = questions[i]

            next_question = i + brainpower + 1
            next_question = num_questions if next_question >= num_questions else next_question

            dp[i] = max(dp[i+1], points + dp[next_question])
        return dp[0]
