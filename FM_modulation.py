from pylab import *

def AMmod(sample_rate, carrier_frequency, modulation_frequency, modulation_amplitude):

    t = []
    am = []
    
    for i in range(int(sample_rate)):
        dt = i/sample_rate
        mod_sig = cos(2*pi*modulation_frequency*dt)
        carrier_sig = cos(2*pi*carrier_frequency*dt)
        dam = carrier_sig*(1+modulation_amplitude*mod_sig)/2
        t.append(dt)
        am.append(dam)
    return t, am

def FMmod(sample_rate, carrier_frequency, modulation_freqeuncy, modulation_index):

    fm_integral = 0
    
    t = []
    fm = []

    for i in range(int(sample_rate)):
        dt = i/sample_rate 
        mod_sig = cos(2*pi*modulation_frequency*dt)
        fm_integral += mod_sig* modulation_index / sample_rate
        dfm = cos(2*pi*carrier_frequency*(dt+fm_integral))
        t.append(dt)
        fm.append(dfm)
    return t, fm

sample_rate = 1000.0
carrier_frequency = 16
modulation_frequency = 2
modulation_index = 0.5

t, fm = FMmod(sample_rate, carrier_frequency, modulation_frequency, modulation_index)

figure(1)
plot(t,fm)
ylim(-1.2,1.2)
gcf().set_size_inches(4,3)
savefig('simple_fm_generator.png')

t, fm = AMmod(2000.0, 25, 3, 2)

figure(2)
plot(t,fm)
ylim(-1.2,1.2)
gcf().set_size_inches(4,3)
savefig('simple_am_generator.png')
show()

