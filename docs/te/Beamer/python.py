\section{Apéndice 1. Programa Python}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\begin{frame}

\frametitle{Apéndice 1. Programa Python}
\begin{definicion}

En este capítulo se pasará a mostrar el código mediante el cual se implemento el polinomio de Newton para la funcion $f(x)=e ^ x$.
\end {definicion}

\end{frame}
%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\subsection{Almacenamiento de x}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\begin{frame}

\frametitle{Almacenamiento de x}

\begin{itemize}
\item
En este fragmento de código se introducen las x y se muestran por pantalla:\par

x = [ ]\par
for i in range (0,5):\par
  ..if i == 0:\par
    ....xi = 0.00\par
  ..else:\par
    ....xi = xi + 1\par
  ..x += [xi]\par
print x 

\end{itemize}

\end{frame}
%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\subsection{Almacenamiento de f[x]}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\begin{frame}

\frametitle{Almacenamiento de f[x]}
\begin{itemize}
\item
A continuación se calculan a partir de los valores de x, los valores de f[x] y se imprimen por pantalla:\par

fx = [ ]\par
for i in range (0,5):\par
    ..fxi = e**x[i]\par
    ..fx += [fxi]\par
print fx 

\end{itemize}
\end{frame}
%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\subsection{Diferencias divididas}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


\begin{frame}

\frametitle{Diferencias dividas}
\begin{itemize}
\item
En este fragmento se calcularán las diferencias divididas y se mostrarán por pantalla:\par

d = [ ]\par
for i in range (0,5):\par
  ..if i == 0:\par
    ....di = fx[i]\par
  ..else:\par
    ....di = (fx[i] - fx[i-1])/(x[i] - x[i-1])\par
  ..d += [di]\par

a = [d[0], d[1], (d[2]-d[1])/(x[2]-x[0]), (d[3]-d[2]+d[1]-d[2])/(x[3]-x[0]), 
(d[4]-d[3]+d[2]-d[3]+d[2]-d[3]+d[2]-d[1])/(x[4]-x[0])]\par

print a 
\end{itemize}
\end{frame}


%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\subsection{Partes literales del polinomio}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


\begin{frame}

\frametitle{Partes literales}
\begin{itemize}
\item
Por último se calcularán las partes literales del polinomio en x = 0.43:\par

y = 0\par
l = [ ]\par
valorx = 0.43\par
for i in range (0,5):\par
  ..li = 1\par
  ..if i == 0:\par
    ....li = 1\par
  ..else:\par
    ....for j in range (0,i):\par
      ......li = li*(valorx-x[j])\par
      ......j+=1\par
  ..l = l + [li]\par
print l \par

\end{itemize}
\end{frame}
%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\subsection{Valores}

%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


\begin{frame}

\frametitle{Valores}
\begin{itemize}
\item
Por último se mostrarán por pantalla los resultados del experimento\par

valorpol = 0\par

for i in range (0,5):\par
  ..valorpol += a[i] * l[i]\par

print '\%.35f' \%valorpol Imprime el valor del polinomio con la x que le hemos dado\par
print '\%.35f' \%(e**valorx)  Imprime el valor real de la función con el valor de x que se asigna\par
print '\%.35f' \%(abs(valorpol-real)) Imprime el error cometido por el polinomio

\end{itemize}
\end{frame}