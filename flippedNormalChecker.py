import maya.cmds as cmds

def get_face_normal(face):
    face_normal = cmds.polyInfo(face, fn=True)
    parts = face_normal[0].split()
    normal_vector = parts[-3:]
    return [float(x) for x in normal_vector]

def get_face_center(face):
    face_vertex = cmds.xform(face, q=True, ws=True, t=True)
    face_center = [sum(face_vertex[i::3]) / (len(face_vertex) / 3) for i in range(3)]
    return face_center
def main():
    print(get_face_normal('pCube1.f[1]'))
    print(get_face_center('pCube1.f[1]'))
if __name__ == "__main__":
    main()