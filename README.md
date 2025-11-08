# Navier-Stokes
## By Alex Reutiman and Caleb McIntyre, with help from Mr. Proctor and B. Hamilton, Ph.D.

Abstract:Proving or giving a counter-example of the statement that given a starting vector field $u:\mathbb R^3\to\mathbb R^3$, there exists a vector velocity and a scalar pressure field, which are smooth and globally defined, that solve the Navier-Stokes equations.

The first of the equations you can use when proving the abstract is the mass-continuity equation, that being
$$\frac{\mathrm Dm}{\mathrm Dt}=\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\textbf{u})=0,$$
where the material derivative $\frac{\mathrm D\textbf{u}}{\mathrm Dt}=\frac{\partial\textbf{u}}{\partial t}+\textbf{u}(\nabla\cdot\textbf{u})$. For simplicity, all material derivatives will be replaced with their partial derivative forms. The other equation used (the Navier-Stokes momentum equation) is defined as
$$\rho\left(\frac{\partial\textbf{u}}{\partial t}+\textbf{u}(\nabla\cdot\textbf{u})\right)=-\nabla p+\nabla\cdot\mu^\dagger+\nabla[\zeta(\nabla\cdot\textbf{u})]+\rho\textbf{a}$$
where \(\mu^\dagger\) is defined as
$$\mu\left[\nabla\textbf{u}+(\nabla\textbf{u})^\mathrm T-\frac23(\nabla\cdot\textbf{u})\textbf{I}\right].$$
Assuming conservation of mass, however, the left side of the equation becomes
$$\frac{\partial}{\partial t}(\rho\textbf{u}+\nabla\cdot(\rho\textbf{u}\otimes\textbf{u})),$$
giving
$$\frac{\partial}{\partial t}(\rho\textbf{u})+\nabla\cdot\left[\rho\textbf{u}\otimes\textbf{u}+[p-\zeta(\nabla\cdot\textbf{u})]\textbf{I}-\mu^\dagger\right]=\rho\textbf{a}.$$
Another equation we can use, due to how the Millenium Prize Problem only accounts for <i>incompressible</i> fluids is
$$\nabla\cdot u=\frac{\partial u_x}{\partial x}+\frac{\partial u_y}{\partial y}+\frac{\partial u_z}{\partial z}$$