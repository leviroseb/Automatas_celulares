import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import colors

def estado_inicial_aleatorio(n_celdas=100, n_generaciones=100):
    pr_columna=np.random.random_integers(1,2,size=(1,n_celdas))
    espacio=np.zeros(shape=(n_generaciones,n_celdas))
    espacio[0]=pr_columna
    return espacio

def iniciar(n_celdas=0, n_generaciones=100, regla={}):
    estado_inicial=estado_inicial_aleatorio(n_celdas,n_generaciones)
    cmap=colors.ListedColormap(['white','blue','grey'])
    bounds=[0,1,2,2]
    norm=colors.BoundaryNorm(bounds,cmap.N)
    fig=plt.figure()
    frame=plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    grid=plt.imshow(estado_inicial,interpolation='nearest',cmap=cmap,norm=norm)
    ani=animation.FuncAnimation(fig,sig_generacion,fargs=(grid,estado_inicial,regla),
        frames=n_generaciones-1,interval=50,blit=False)
    plt.show()

def sig_generacion(i,grid,estado_inicial,regla):
    generacion_actual=estado_inicial[i]
    nuevo_estado=estado_inicial.copy()
    nueva_generacion=proceso(generacion_actual,regla)
    nuevo_estado[i+1]=nueva_generacion
    grid.set_data(nuevo_estado)
    estado_inicial[:]=nuevo_estado[:]
    return grid

def proceso(generacion, regla):
    nueva_generacion=[]
    for i, celda in enumerate(generacion):
        vecinos=[]
        if i==0:
            vecinos=[generacion[len(generacion)-1],celda,generacion[1]]
        elif i==len(generacion)-1:
            vecinos=[generacion[len(generacion)-2],celda,generacion[0]]
        else:
            vecinos=[generacion[i-1],celda,generacion[i+1]]
        
        nueva_generacion.append(regla[tuple(vecinos)])
    return nueva_generacion

def generar_regla(regla):
    regla_str=format(regla,'#010b')[2:]
    regla={
        (2,2,2):int(regla_str[0])+1,
        (2,2,1):int(regla_str[1])+1,
        (2,1,2):int(regla_str[2])+1,
        (2,1,1):int(regla_str[3])+1,
        (1,2,2):int(regla_str[4])+1,
        (1,2,1):int(regla_str[5])+1,
        (1,1,2):int(regla_str[6])+1,
        (1,1,1):int(regla_str[7])+1
    }

    return regla


def main():
    n_celdas=int(input("Numero de celdas: "))
    n_generaciones=int(input("Numero de generaciones: "))
    regla=int(input("Numero de regla: "))
    regla=generar_regla(regla)
    estado_inicial=iniciar(n_celdas,n_generaciones,regla)

if __name__=='__main__':
    main()
