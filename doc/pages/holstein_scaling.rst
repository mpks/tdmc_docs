Holstein model scaling
----------------------

When writing the procedure for time evolution, the original
1D Holstein Hamiltonian

.. math::

    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                  \hat{c}_{i}^\dagger\hat{c}_{i+1} + {\rm h.c.}
              \right) 
              + g \sum_{i=1}^{N} Q_i\left(
                                        \hat{c}_{i}^\dagger\hat{c}_{i} - 1/2
                                    \right)
              + \frac{K}{2} \sum_{i=1}^{N} Q_i^2
              + \frac{1}{2M} \sum_{i=1}^{N} P_{i}^2

was scaled

.. math::

    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                  \hat{c}_{i}^\dagger\hat{c}_{i+1} + {\rm h.c.}
              \right) 
              + \frac{g}{\sqrt{K}} \sum_{i=1}^{N} \tilde{Q}_i
                \left(
                      \hat{c}_{i}^\dagger\hat{c}_{i} - 1/2
                \right)
              + \frac{1}{2} \sum_{i=1}^{N} \tilde{Q}_i^2
              + \frac{K}{2M} \sum_{i=1}^{N} \tilde{P}_{i}^2,


where :math:`\tilde{Q}_{i} = \sqrt{K} Q_{i}`
and :math:`\tilde{P}_{i} = \frac{1}{\sqrt{K}} P_{i}`.
By introducing new variables :math:`\lambda =\frac{g^2}{4K\gamma}`
and :math:`\omega_{0} = \sqrt{K/M}` the given Hamiltonian transforms

.. math::
    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                    \hat{c}_{i}^\dagger\hat{c}_{i+1} + {\rm h.c.}
              \right) 
              + 2\sqrt{\lambda \gamma} \sum_{i=1}^{N} \tilde{Q}_i\left(
                         \hat{c}_{i}^\dagger\hat{c}_{i} - 1/2
                         \right)
              + \frac{1}{2} \sum_{i=1}^{N} \tilde{Q}_i^2
              + \frac{\omega_{0}^2}{2} \sum_{i=1}^{N} \tilde{P}_{i}^2.

If we substitute the initial phonon position 
:math:`Q_i = \frac{1}{g}\Delta_i`, then
:math:`\tilde{Q}_i = \sqrt{K}Q_i = \frac{\sqrt{K}}{g}\Delta_i = \frac{1}{2\sqrt{\lambda\gamma}}\Delta_i` so the Hamiltonian transforms
into

.. math::

    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                    \hat{c}_{i}^\dagger\hat{c}_{i+1} + {\rm h.c.}
              \right) 
              + \sum_{i=1}^{N} \Delta_i\left(
                         \hat{c}_{i}^\dagger\hat{c}_{i} - 1/2
                         \right)
              + \frac{1}{8\lambda\gamma} \sum_{i=1}^{N} \Delta_i^2
              + \frac{\omega_{0}^2}{2} \sum_{i=1}^{N} \tilde{P}_{i}^2.

The original system of equations of motion

.. math::

    \frac{d}{dt} Q_i(t) = P_i(t)/M

.. math::

    \frac{d}{dt} P_i(t) = -K Q_i(t) - g(n_i(t) - 1/2)

then transforms into

.. math::
    \frac{d}{dt} \tilde{Q}_i(t) = \omega_0^2 \tilde{P}_i(t)

.. math::
    \frac{d}{dt} \tilde{P}_i(t) = -\tilde{Q}_i(t) -
    2\sqrt{\lambda\gamma}(n_i(t) - 1/2)

Finally, using substitution 
:math:`\tilde{Q}_i = \frac{1}{2\sqrt{\lambda\gamma}}\Delta_i` and
:math:`2\sqrt{\lambda\gamma}\tilde{P}_i = \pi_i`
we get our final equations of motion for the Holstein model

.. math::
    \frac{d}{dt} \Delta_i(t) = \omega_0^2 \pi_i(t)

.. math::
    \frac{d}{dt} \pi_i(t) = -\Delta_i(t) - 
    4\lambda\gamma(n_i(t) - 1/2)

Note that in the old Fortran code, for the zero temperature,
the Hamiltonian was implemented using equations of motion with
:math:`\Delta_i` and :math:`\pi_i`, while the code for the nonzero
temperature was implemented using 
:math:`\tilde{Q}_i` and :math:`\tilde{P}_i`. The convention in the present
package is to use the Hamiltonian defined in terms of
:math:`\tilde{Q}_i` and :math:`\tilde{P}_i`. In the code they are
represented as ``qi`` and ``pi``. Additionally, in ``holstein.py``
there is a function ``q0()`` which returns the coordinate
:math:`\Delta_i`. This is used for comparison with the old code, but
also because it represents the gap energy.
