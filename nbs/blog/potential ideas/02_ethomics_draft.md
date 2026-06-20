# Contextualized Ethomics — full draft (embargoed)

A hungry animal does not just "eat more." It moves differently. It searches differently. It takes different kinds of meals. It changes its behavior after eating. Hunger and satiety are not single actions; they are whole-body states.

That was the starting point for this project. In feeding research, it is very easy to pick one measurement — how much an animal ate, how often it visited food, how quickly it approached food — and declare that a neuron "causes hunger" or "causes satiety." But this can be misleading. A manipulation might make an animal contact food more often because it is hyperactive. Another might reduce food intake because the animal cannot move properly. A third might change meal number but not meal size. If we only look at the metric that changed, we can tell the wrong story.

I wanted to build a way around that problem. Instead of asking whether a neural manipulation changes one feeding readout, we asked whether it recreates a complete, biologically meaningful state transition.

To do that, we first needed a ground truth. In flies, starvation is a real and well-understood transition into hunger. Refeeding is a real transition toward satiety. So we measured what these natural transitions look like across many behavioral dimensions at once: total food volume, meal size, meal number, meal duration, feeding speed, walking speed, food-port occupancy, post-meal slowing, and other movement features. This gave us a multidimensional fingerprint of authentic hunger and satiety.

We built this around an automated behavioral system called **Espresso**, which tracks tiny liquid meals in individual flies while simultaneously tracking locomotion. That combination mattered. Feeding is not just consumption; it is embedded in movement, search, approach, and post-meal behavioral change. Espresso let us measure those features together, rather than treating feeding as a single number.

The conceptual method was what I call **contextualized ethomics**: high-dimensional behavior interpreted in relation to a known biological context. We formalized this as **DESTRA** — delta ethomic state-transition recapitulation assessment. In plain language, DESTRA asks: when I perturb a neural circuit, does the resulting behavioral profile point in the same direction as a real state transition?

This reframes the experiment. The question is no longer only "did this neuron change feeding?" The stronger question is "did this neuron move the animal along the authentic hunger–satiety axis?"

That distinction turned out to be crucial. Some serotonergic manipulations appeared feeding-related if judged by one metric. For example, one serotonin driver made flies eat more by increasing how often they fed. If we stopped there, we might call it a hunger circuit. But the broader behavioral profile told a different story: the flies also showed locomotor and food-seeking patterns that did not match natural hunger. The intervention produced a disjointed behavioral state, not an authentic hunger transition.

By contrast, neurons marked by the **Tryptophan hydroxylase enhancer, Trhn**, behaved like true state-control neurons. Activating these neurons in hungry flies pushed behavior toward satiety: flies ate less, primarily by taking smaller meals, and their movement patterns shifted away from hunger-like food seeking. Inhibiting the same neurons in fed flies pushed behavior in the opposite direction, toward hunger-like consumption and locomotion. Across many measured features, Trhn manipulations best matched the natural hunger–satiety transitions.

This is the central point of the paper: the right circuit is not necessarily the one that changes the biggest single metric. It is the one whose whole behavioral signature aligns with the state transition we already know is real.

The approach also made it possible to track the biology deeper. By comparing experimental profiles against the natural state-transition ground truth, we could identify which interventions captured authentic satiety or hunger, then anatomically narrow the responsible neurons. The strongest evidence pointed to serotonergic neurons in the ventral nerve cord, with further experiments implicating sugar transporter 2 as part of the mechanism linking nutritional state to serotonergic feeding control.

For me, this project is about more than fly feeding. It is a general argument about measurement. Complex biological states should not be inferred from cherry-picked readouts. They should be benchmarked against known transitions, measured across many dimensions, and interpreted as profiles rather than isolated effects.

Contextualized ethomics is my attempt to make that principle practical: first define the natural state transition, then measure behavior broadly, then ask which interventions genuinely recapitulate the state. In this paper, that approach revealed a serotonergic satiety circuit. More broadly, it provides a framework for separating real state control from behavioral artifacts.
