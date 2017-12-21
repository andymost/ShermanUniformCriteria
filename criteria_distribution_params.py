import numpy.random as n_rand
from sherman import sherman_w_modified, sherman_w_normalized



def estimate_params_normalized():
    samples_sizes = [20, 50, 100, 200, 1000, 2000]
    samples_count = 1000

    sample_size_num = 0

    while sample_size_num < len(samples_sizes):
        sample_size = samples_sizes[sample_size_num]
        file = open('./output/%d_%d_%s.dat' % (sample_size, samples_count, 'normalized'), 'w')
        file.write('Normalaized %d\n0 %d\n' % (sample_size, samples_count))
        sample_index = 0

        while sample_index < samples_count:
            n_rand.seed(sample_index)
            sample = n_rand.sample(sample_size)
            file.write(str(sherman_w_normalized(sample)))
            file.write('\n')
            sample_index = sample_index + 1
        file.close()

        sample_size_num = sample_size_num + 1


def estimate_params_modified():
    samples_sizes = [20, 50, 100, 200, 1000, 2000]
    samples_count = 1000

    sample_size_num = 0

    while sample_size_num < len(samples_sizes):
        sample_size = samples_sizes[sample_size_num]
        file = open('./output/%d_%d_%s.dat' % (sample_size, samples_count, 'modified'), 'w')
        file.write('Modified %d\n0 %d\n' % (sample_size, samples_count))
        sample_index = 0

        while sample_index < samples_count:
            n_rand.seed(sample_index)
            sample = n_rand.sample(sample_size)
            file.write(str(sherman_w_modified(sample)))
            file.write('\n')
            sample_index = sample_index + 1
        file.close()

        sample_size_num = sample_size_num + 1