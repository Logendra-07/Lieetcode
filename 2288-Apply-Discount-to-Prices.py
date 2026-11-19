class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        k=sentence.split()
        for i in range(len(k)):
            if k[i][0]=="$":
                if k[i][1:].isdigit():
                    cost=float(k[i][1:])
                    dis_cost=cost*(1-discount/100)
                    k[i]=f"${dis_cost:.2f}"
        return " ".join(k)