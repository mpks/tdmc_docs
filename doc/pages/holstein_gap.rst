Holstein model gap
----------------------

The gap for the Holstein model at the zero temperature can be
computed numerically. Starting from the Holstein Hamiltonian

.. math::
    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                \hat{c}_{i}^\dagger\hat{c}_{i+1} + {\rm h.c.}
              \right) 
              + \sum_{i=1}^{N} \Delta_i
                  \left(
                      \hat{c}_{i}^\dagger\hat{c}_{i} - 1/2
                  \right)
              + \frac{1}{8\lambda\gamma} \sum_{i=1}^{N} \Delta_i^2
              + \frac{\omega_{0}^2}{2} \sum_{i=1}^{N} \tilde{P}_{i}^2.

and we assume :math:`\tilde{P}_i=0` for every :math:`i`, with initial state
set as :math:`\Delta_i =(-1)^i\Delta`, we get

.. math::
    \hat{H} = -\gamma \sum_{i=1}^{N} 
              \left(
                  \hat{c}_{i}^\dagger\hat{c}_{i+1} + 
                  \hat{c}_{i+1}^\dagger\hat{c}_{i}
              \right) 
              + \Delta \sum_{i=1}^{N} (-1)^i 
                         \hat{c}_{i}^\dagger\hat{c}_{i} 
              + \frac{1}{8\lambda\gamma} N\Delta^2

We want to transform this Hamiltonian into the inverse
space by transforming the annihilation and creation operators

.. math::
    \hat{c}_{m}^\dagger =\frac{1}{\sqrt{N}}
       \sum_{k} e^{-ikm}\hat{c}_k^\dagger,

and 

.. math::
    \hat{c}_{m} =\frac{1}{\sqrt{N}}
       \sum_{k} e^{ikm}\hat{c}_k^\dagger.

Assuming :math:`\gamma` is real, the first term transforms into

.. math::
    -\gamma\frac{1}{N}\sum_{m=1}^{N}
     \sum_k\sum_{k'}
     \left(
           e^{-imk}e^{i(m+1)k'}\hat{c}^{\dagger}_{k}
           \hat{c}_{k'}
     +
           e^{-i(m+1)k}e^{imk'}\hat{c}^{\dagger}_{k}
           \hat{c}_{k'}
     \right)

or

.. math::
    -\gamma\frac{1}{N}\sum_{m=1}^{N}
    \sum_k\sum_{k'}
    \left(
         e^{-im(k-k')}e^{ik'}\hat{c}^{\dagger}_{k}
         \hat{c}_{k'}
    +
         e^{-im(k-k')}e^{-ik}\hat{c}^{\dagger}_{k}
         \hat{c}_{k'}
    \right)

For large :math:`N`, the Kronecker delta function can be written as 

.. math::
    \delta_{kk'} = \frac{1}{N}\sum_{m=1}^{N}e^{im(k-k')},

where :math:`k=\frac{2\pi}{N}r` and :math:`k'=\frac{2\pi}{N}r'` and
:math:`r` and :math:`r'` are integers going from :math:`0` to :math:`N-1`.
The sums over
:math:`m` and :math:`k'` in the first term disappear after the previous
transformation and we get

.. math::
    -\gamma \sum_k
    (e^{ik} + e^{-ik})\hat{c}^{\dagger}_{k}
    \hat{c}_{k}
    = -
    \sum_k (2\gamma\cos k) \hat{c}^{\dagger}_{k} \hat{c}_{k}

The second term transforms as 

.. math::
    \Delta\sum_{m=1}^{N}(-1)^{m}\hat{c}^\dagger_{m}\hat{c}_{m}
    =
    \frac{1}{N}\sum_{m=1}^{N}
    \sum_{k}\sum_{k'}e^{-im(k-k')}e^{im\pi}\hat{c}_{k}^\dagger
    \hat{c}_{k} =
    \sum_{k}\sum_{k'}\delta_{k,k'+\pi}
    \hat{c}_{k}^\dagger\hat{c}_{k'} = \Delta\sum_{k}
     \hat{c}_{k}^\dagger\hat{c}_{k+\pi}

Here, the vector :math:`k` runs from zero to :math:`2\pi` in discrete steps
of :math:`\frac{2\pi}{N}`. Due to the periodicity of the Brillouin
zone, and the fact that for :math:`k`-s above :math:`\pi` we have 
:math:`k+\pi \rightarrow k-\pi`, the above sum can be divided into
two sums 

.. math::
    \Delta \left(\sum_{k\le\pi}\hat{c}^\dagger_{k}\hat{c}_{k+\pi}
                 +
                 \sum_{k>\pi}\hat{c}^\dagger_{k}\hat{c}_{k+\pi}
           \right) =
    \Delta \left(\sum_{k\le\pi}\hat{c}^\dagger_{k}\hat{c}_{k+\pi}
                 +
                 \sum_{k>\pi}\hat{c}^\dagger_{k}\hat{c}_{k-\pi}
           \right) =

.. math::
    \Delta \left(\sum_{k\le\pi}\hat{c}^\dagger_{k}\hat{c}_{k+\pi}
                 +
                 \sum_{k\le\pi}\hat{c}^\dagger_{k+\pi}\hat{c}_{k}
           \right) 


In a similar way, assuming :math:`\epsilon(k)=-2\gamma\cos k` the 
sum for the onsite terms can be divided into two parts 

.. math::
    \sum_{k\le\pi}\epsilon(k)\hat{c}^\dagger_{k}\hat{c}_{k}
        +
    \sum_{k>\pi}\epsilon(k)\hat{c}^\dagger_{k}\hat{c}_{k} =
    \sum_{k\le\pi}\epsilon(k)\hat{c}^\dagger_{k}\hat{c}_{k}
    +
    \sum_{k\le\pi}\epsilon(k+\pi)\hat{c}^\dagger_{k+\pi}
     \hat{c}_{k+\pi} =

.. math::
    \sum_{k\le\pi}\epsilon(k)\hat{c}^\dagger_{k}\hat{c}_{k}
    -\sum_{k\le\pi}\epsilon(k)\hat{c}^\dagger_{k+\pi}
     \hat{c}_{k+\pi} 

The last sign change comes from the fact that 
:math:`\cos(k+\pi) = -\cos k`. Since all sums now run for :math:`k<\pi` the
Brillouin zone is now reduced and the Hamiltonian can be
written as a :math:`2\times 2` matrix

.. math::
  \sum_{k\le\pi}
  \begin{pmatrix} \hat{c}_{k}^\dagger & \hat{c}_{k+\pi} 
  \end{pmatrix}
  \begin{pmatrix} \epsilon(k) & \Delta \\
                  \Delta & -\epsilon(k)
  \end{pmatrix}
  \begin{pmatrix} \hat{c}_{k} \\
                  \hat{c}_{k+\pi}
  \end{pmatrix}

For each :math:`k` the matrix can be diagonalized and the
eigenenergies can be computed 

.. math::
    {\rm det}
    \begin{vmatrix} \epsilon(k) -\lambda_k & \Delta \\
                  \Delta & -\epsilon(k) - \lambda_k
    \end{vmatrix}
    = -(\epsilon(k) - \lambda_k)(\epsilon(k) + \lambda_k) -
    \Delta^2 = \lambda_k^2 - \epsilon(k)^2 - \Delta^2 = 0.

From here we get the eigen energies as 

.. math::
    \lambda_{k,\pm} = \pm \sqrt{\epsilon(k)^2 + \Delta^2}.

This corresponds to two bands for each :math:`k`, and the bands are
separated by the gap :math:`2\Delta` at :math:`k = \pi`.
The total energy for a half-filled system is then obtained by
summing over the lower band and adding the extra constant 

.. math::
    E_{\rm tot} = -\sum_{k\le\pi} \sqrt{\epsilon(k)^2 + \Delta^2} +
     \frac{N\Delta^2}{8\lambda\gamma}

The band gap :math:`\Delta` for a given coupling :math:`\lambda` can be
determined by minimizing the derivative of total energy
:math:`\partial E_{\rm tot} /\partial \Delta` with respect to
:math:`\Delta`.

.. math::
    \frac{\partial E_{\rm tot}}{\partial \Delta} =
    -\sum_{k<\pi}
      \frac{\Delta}{\sqrt{\epsilon(k)^2 + \Delta^2}}
      +
      \frac{N\Delta}{4\lambda\gamma} = 0

From here we get two solutions for the gap, one is 
:math:`\Delta = 0` which we discard. The other is 

.. math::

    \sum_{k\le\pi}
    \frac{1}{N}
    \frac{4\lambda\gamma}{\sqrt{\epsilon(k)^2 + \Delta^2}} - 1 = 0


The gap is computed numerically. We set the upper and lower
limit for the gap :math:`\Delta_{\rm max}` and 
:math:`\Delta_{\rm min}` and compute the derivative using the previous
equation. If the derivative is negative, the :math:`\Delta` needs to
get smaller (because the derivative scales as 
:math:`\frac{1}{\Delta}`), on the other end, if the derivative is
positive, the :math:`\Delta` needs to increase. By moving the limits
:math:`\Delta_{\rm min}` and :math:`\Delta_{\rm max}` we compute the
:math:`\Delta` which gives the zero of the first energy derivative.
