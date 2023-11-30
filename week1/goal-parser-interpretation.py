class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)-1):
            if command[i]=='(' and command[i+1]==")":
                ans+="o"
            elif command[i]!='(' and command[i]!=")":
                ans+=command[i]
        if command[-1]!=")":
            ans+=command[-1]
        return ans
                
        