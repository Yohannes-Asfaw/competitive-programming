class Solution:
    def average(self, salary: List[int]) -> float:
        maxsalary=max(salary)
        minsalary=min(salary)
        sum1=0
        for i in salary:
            if i!=maxsalary and i!=minsalary:
                sum1+=i
        return sum1/(len(salary)-2)
        