import svdRec

if __name__ == "__main__":
    print ('This is main of module "hello.py"')
    myMat = svdRec.mat(svdRec.loadExData())
    svdRec.recommend(myMat, 1, estMethod=svdRec.svdEst)