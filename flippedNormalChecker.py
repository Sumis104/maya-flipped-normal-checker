import maya.cmds as cmds

def get_face_normal(face):
    face_normal = cmds.polyInfo(face, fn=True)
    parts = face_normal[0].split()
    normal_vector = parts[-3:]
    return [float(x) for x in normal_vector]

def main():
    print(get_face_normal('pCube1.f[1]'))

if __name__ == "__main__":
    main()