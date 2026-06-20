
# Tuim


## Motivation

The project goal is to fly a drone, both piloting and in autonomous flight.

In order to do so, we will need to explore the technologies that make modern autonomous systems possible. The first technology is the F' framework from NASA [^10]. The reason to chose this framework is that it was proven in more than one project and is open source. We have the opportunty to learn from the same framework that was part of the Ingenuity Mars helicopter [^11].

## F' Hello Tutorial

To have a first a contact with the F', we suggest you to follow the Hello Tutorial [], using Github Codespaces []. This experience will let you install software and libraries on a Linux computer, using cloud resources.

We may find other similar frameworks, but we recommend to stay with F' so we can all share a similar experience.

## Required Equipment

To have  first contact with drones, we suggest you to get a Radiomaster Pocket radio controller and log some hours on SkyDive drone simulator.

You can adapt and use any controller and simulator available to you.

All dwof these decisions were made from the perspective of someone with no previous flight experience and no existing drone equipment. We chose to invest first in a radio controller because it provides practical experience and a better understanding of drone piloting. At the same time, we decided to postpone the decision of whether to buy or build a real drone.

To fly a drone, we need two main components: a drone and a radio controller.

A real drone operates on batteries, has a limited flight time, and its operation involves some risk of damage to equipment. A drone simulator, on the other hand, allows us to learn how to pilot a drone without the risk of crashes and without the limitations imposed by battery life.

For these reasons, we decided to start with a simulator rather than a real drone. We chose FPV.SkyDive [^1], a free drone simulator available on Steam.^1

In the future, we may buy or build a real drone. At this stage, however, a simulator provides more benefits for a novice pilot than a physical aircraft.

A radio controller also operates on batteries, but it differs significantly from a gamepad, keyboard, or mouse. While a simulator can be controlled using those devices, doing so would not provide an experience that transfers well to real drone piloting.

Therefore, we decided to purchase a dedicated radio controller. This allows us to learn using the same type of interface employed in real drone operations and preserves the possibility of connecting the controller to a real drone in the future.

We chose the RadioMaster Pocket [^2], an affordable and widely recommended entry-level radio controller for novice pilots. The controller was purchased from an online seller [^3]. 

The controller came with no batteries included. We bought two batteries from a local seller [^4]. The model required is flat top, rechargeable, no chip.


## Radio Controller

Radion controller most important activities early on are: (a) setup and bind to a drone [^5][^6] and (b) setup a simulator [^7].

The first hours operating a radio controller can be intimidating. There is a lot of concepts for a novice to absorb. Staying away from the controller will not help.
Bute the larger issues are the hazards of using the equipament itself. 

Using a simulator, disabling the radio will remove two of the possible hazards. First, the controller operator torso must keep 20 cm, like a extended palm, away from the controller. The radio controller works emiting radio waves and the manual advises to keep a safe distance. Second, if the radio is on, the antena must be extended. The manual warns about damage if the radio on and the antena is not extended. 

So, while using the simulator, always check if the radio is disabled and these two radio wave related hazards are eleminated.

Bateries are neeed, even when using the radio controller with the simulator. Actually, we have not explored the option of using two separate cables for data and energy at the same time. But we believe the radio controller was designed to be used with batteries on.

Batteries have some hazards that could damage the controller. A faulty battery can leak acid, blow, or catch fire. Batteries should not stay on the controller if it is not in use for some weeks, batteries can leak acid over time. It is easy to forget a device stored with batteries in.

During setup, battery polarity can become an issue, because both poles are flat. We found negative pole signs on battery and the controller case. Wrong polarity could damage the controller.

Lastly, the controller has a built-in charger, and it is important to not let the batteries charge unattended or near flamable material.


Batteries

USB Cable

Antena 

USB Adapter from a local seller.

Controller Configuration

Date and time

Disable Radio for Simulator Use saves battery

Games

Throttle and Arm

FPV Drone Model

Charging

USB Charge bottom port

USB HID top port




## Drone Simulator

Callibration



[^1]: https://store.steampowered.com/app/1278060/FPV_SkyDive__FPV_Drone_Simulator/

[^2]: https://radiomasterrc.com/products/pocket-radio-controller-m2
[^3]: https://pt.aliexpress.com/item/1005005908395212.html
[^4]: https://www.eletronicasystem.com.br/produto/bateria-3-7v-2600mah-li-ion-industrial-green-cr18650-6-4x1-8cm-pilha-3-7v

[^5]: https://www.youtube.com/watch?v=GgaWMvAHZi8
[^6]: https://www.youtube.com/watch?v=YRU9JoUw9Jw

[^7]: https://www.youtube.com/watch?v=l8S1CF4_K7Q

[^10]: https://fprime.jpl.nasa.gov
[^11]: https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/

[^30]: https://oscarliang.com/setup-radiomaster-pocket/
[^20]: https://cdn.shopify.com/s/files/1/0701/8066/7584/files/Pocket_A1.8.pdf?v=1770617495

[^40]: https://fprime.jpl.nasa.gov/latest/tutorials-hello-world/docs/hello-world/
