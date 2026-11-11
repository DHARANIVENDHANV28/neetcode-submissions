class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        
        HashMap = {feat:0 for feat in features}
       
        for res in responses:
            words = set(res.split())
            for feat in features:
                if feat in words:
                    HashMap[feat]+=1
        
        return sorted(features,key=lambda x:-HashMap[x])


            
