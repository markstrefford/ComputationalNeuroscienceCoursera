"""
Created on Wed Apr 22 15:21:11 2015

@author: rkp

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA

    Returns:
        spike-triggered average for specified number of timesteps before spike"""

    sta = np.zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times)

    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    #
    # Your code goes here.
    per_spike_sta = np.zeros((num_spikes, num_timesteps))
    spike_id = 0
    for spike_time in spike_times:

        # Compute average of all spike_time - 299
        # Compute average of all spike_toime - 298
        # ...
        stimuli = stim[spike_time-num_timesteps:spike_time]
        per_spike_sta[spike_id] = stimuli
        spike_id += 1

    sta = np.mean(per_spike_sta, axis=0)

    return sta
