import math

# class for events of repairable systems
class Event:
    def __init__(self, name="Event", fr=0, mttr=0, rr=0, q=0, w=0, t=1):
        self.name = name    # event name
        self.fr = fr        # failure rate
        self.mttr = mttr    # mean time to repair
        if mttr:
            self.rr = 1/mttr
        else:
            self.rr = rr    # repair rate
        if q and w:
            self.q = q      # unavailability
            self.w = w      # failure frequency
        else:
            self.q = (fr)/(fr+self.rr)*(1-math.exp(-(fr+self.rr)*t))
            self.w = (1-self.q)*fr
    
    def print_stats(self):
        print(self.name)
        print("---------------")
        if self.fr and self.mttr:
            print("FR   =", format(self.fr, '.2e'))
            print("MTTR =", self.mttr)
        if self.fr and not self.rr:
            print("FR   =", format(self.fr, '.2e'))
            print("RR   =", format(self.fr, '.2e'))
        print("w    =", format(self.w, '.2e'))
        print("Q    =", format(self.q, '.2e'))
        print()

# OR calculation
# example 3 events
# w = w_1*(1-q_2)*(1-q_3) + w_2*(1-q_1)*(1-q_3) + w_3*(1-q_1)*(1-q_2)
# q = 1 - (1-q_1)*(1-q_2)*(1-q_3)
def calc_OR(*argv):
    w = 0.0
    for i in range(len(argv)):
        x = 1
        for j in range(len(argv)):
            if i == j:
                continue
            x = x * (1-argv[j].q)
        w = w + argv[i].w * x
    
    q = 1.0
    for i in range(len(argv)):
        q = q * (1-argv[i].q)
    q = 1 - q
    return w, q

# AND calculation
# example 3 events
# w = w_1*q_2*q_3 + w_2*q_1*q_3 + w_3*q_1*q_2
# q = q_1*q_2*q_3
def calc_AND(*argv):
    w = 0.0
    for i in range(len(argv)):
        x = 1
        for j in range(len(argv)):
            if i == j:
                continue
            x = x * argv[j].q
        w = w + argv[i].w * x

    q = 1.0
    for i in range(len(argv)):
        q = q * argv[i].q
    return w, q

def main():
    try:
        # System life time
        t_sys = 24 * 365 * 10   # 10 years

        # Basis events
        BE1 = Event(name="Basis event 1", fr=0.2e-09, mttr=12, t=t_sys)
        BE2 = Event(name="Basis event 2", fr=0.11e-09, mttr=20, t=t_sys)
        BE3 = Event(name="Basis event 3", fr=0.9e-09, mttr=1, t=t_sys)
        BE4 = Event(name="Basis event 4", fr=0.55e-09, mttr=2, t=t_sys)

        BE1.print_stats()
        BE2.print_stats()
        BE3.print_stats()
        BE4.print_stats()

        # OR & AND calculation for top event
        te1_w, te1_q = calc_OR(BE1, BE2, BE3, BE4)
        te2_w, te2_q = calc_AND(BE1, BE2, BE3, BE4)

        TE1 = Event(name="OR gate", w=te1_w, q=te1_q)
        TE2 = Event(name="AND gate", w=te2_w, q=te2_q)

        print("Top events")
        print("###############")
        TE1.print_stats()
        TE2.print_stats()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
