import maya.cmds as cmds

def get_face_normal(face):
    face_normal = cmds.polyInfo(face, fn=True)
    parts = face_normal[0].split()
    normal_vector = parts[-3:]
    return [float(x) for x in normal_vector]

def get_face_center(face):
    face_vertices = cmds.xform(face, q=True, ws=True, t=True)
    face_center = [sum(face_vertices[i::3]) / (len(face_vertices) / 3) for i in range(3)]
    return face_center
def get_mesh_center(mesh):
    vertex_coords = cmds.xform(mesh + '.vtx[*]', q=True, ws=True, t=True)
    mesh_center = [sum(vertex_coords[i::3]) / (len(vertex_coords) / 3) for i in range(3)]
    return mesh_center
def check_flipped_normals(mesh):
    mesh_center = get_mesh_center(mesh)
    faces = cmds.polyEvaluate(mesh, face=True)
    flipped_faces = []
    for i in range(faces):
        face_name = mesh+'.f['+str(i)+']'
        face_normal = get_face_normal(face_name)
        face_center = get_face_center(face_name)
        outward_vector = [face_center[j] - mesh_center[j] for j in range(3)]
        dot_product = sum(face_normal[j] * outward_vector[j] for j in range(3))
        if dot_product < 0:
            flipped_faces.append(face_name)
    return flipped_faces

def main():
    flipped_faces = check_flipped_normals(cmds.ls(selection=True)[0])
    if flipped_faces:
        cmds.select(flipped_faces)
        print("Flipped normals found", flipped_faces)
        
    else:
        print("No flipped normals found.")

if __name__ == "__main__":
    main()