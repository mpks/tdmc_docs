Example scripts
===============

To propagate the electron-phonon coupled system, it is
important to separate several concepts, namely the
tight-binding system, the external field which is used to drive
it out of equilibrium, and the tight-binding system that is
evolved in time. The ``tdmc`` package has an object for each
of these three. First, we start with the external electric
field. The external electric field defines a vector potential
which is its time integral. The field object is implemented in
the class ``Avec`` located in the file ``field.py``. The class
initializer requires a time-dependent function for the field 
(see the ``make_gauss`` function in ``field.py`` on how to define 
an external field). A simple way to define the field object is

.. code-block:: python

    from tdmc.field import Avec, make_gauss
    gauss = make_gauss(sigma=10, omega=0.1)
    avec = Avec(gauss)

Note the convention is that pump field is usually centered at
zero time moment. 

The static system for each tight-binding Hamiltonian needs to
be implemented separately, together with specific functions
for measuring energy etc. Currently, only 1D Holstein
tight-binding system is implemented in the code. Once
the system is imported and created

.. code-block:: python

    from tdmc.holstein import Chain
    chain = Chain(nx=30, omega=0.01)

one can proceed with time propagation of this system. The 
system is propagated with ``Propagator`` object defined in
``propagator.py`` file. To construct a propagator object, one
needs the tight-binding chain object and the external field
object and other parameters for the time evolution. The
propagator object has the ``propagate()`` function which
is used to advance it to the next time step, and ``test_end()``
function which is used in ``while`` loop.

.. code-block:: python

    p = Propagator(chain, avec, tmin=-300, tmax=300, dt=0.1)
    while p.test_end():
        p.propagate()

The ``p.propagate()`` advances the electronic and phonon systems
in time. One can access the propagated tight-binding systems 
(the ``chain`` object in the example above) with ``p.tb`` and
use its properties to compute different quantities. There
is also parameter ``p.time`` which keeps the track of the
current time step.
