class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for i in operations:
            if i == "+":
                records.append(records[-1] + records[-2])
            elif i == "C":
                records.pop()
            elif i == "D":
                records.append(records[-1] * 2)
            else:              
                records.append(int(i))  

        return sum(records)

        
        