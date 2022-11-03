S = "PythonCode"
slices = [S[:], S[1], S[6], S[9], S[-1],
          S[:4], S[4:7], S[-6:-2], S[-7:-2], S[:-1]]
for i in slices:
    print(i)
