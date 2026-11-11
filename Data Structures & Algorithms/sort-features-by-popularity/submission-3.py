class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        
        HashMap = {feat:0 for feat in features}
        # Output = []

        # for feat in features:
        #     cnt = 0
        #     for res in responses:
        #         if feat in res.split(" "):
        #             cnt += 1
        #     if cnt not in HashMap:
        #         HashMap[cnt] = []
        #     HashMap[cnt].append(feat)
                    
        # for i in range(len(features),-1,-1):
        #     if i in HashMap:
        #         for j in HashMap[i]:
        #             Output.append(j)

        # return Output

        for res in responses:
            words = set(res.split())
            for feat in features:
                if feat in words:
                    HashMap[feat]+=1
        
        return sorted(features,key=lambda x:-HashMap[x])


            
