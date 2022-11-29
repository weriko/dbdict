# NO EDGE CASES TESTED, THIS COULD EXPLODE AT ANY GIVEN MOMENT, DO NOT USE AT PRODUCTION, OR AT ALL
#for fun small project
class DBDict(dict):
    def __init__(self,*arg,**kw):
        super(DBDict, self).__init__(*arg, **kw)
        
    @classmethod    
    def check_iter(self, d):
        try:
            iter(d)
            assert type(d)!=str
            return True
        except:
            return False
        
        
    @classmethod
    def create_group_by(self, data, keys):
        if not self.check_iter(keys):
            keys = [keys]
        buckets = {"__FAILED__":[]}
        for d in data:
            t = d
            for k in keys:
                try:
                    d=d[k]
                except:
                    buckets["__FAILED__"].append(t)
            if not self.check_iter(d): #If key is not an iterable it will just create a bucket per value
                if d in buckets:
                    buckets[d].append(t)
                else:
                    buckets[d] = [t]
            else:
                for i in d:
                    if i in buckets:
                        buckets[i].append(t)
                    else:
                        buckets[i] = [t]
            
        return DBDict(buckets)
    
    def scan(self, query, keys):
        res = []
        for pk in self.keys():
            for v in self[pk]:
                t = v
                for k in keys:
                    try:
                        v = v[k]
                    except:
                        ...
                if query in v:
                    res.append(t)
        return res
        