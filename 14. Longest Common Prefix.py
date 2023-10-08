def longestCommonPrefix(self, strs: List[str]) -> str:
        maior_index = 0
        somatorio = 0
        index = ''
       
        for g in range(len(strs[0])):
            for i in strs:
                nome = strs[0][:g+1]
                bol = nome in i[:g+1]
                if (bol) and (nome != ''):
                    somatorio += 1
                if (len(nome) > maior_index) and (somatorio == len(strs)):
                    maior_index = len(nome)
                    index=nome
            somatorio = 0
       
        return (index)
