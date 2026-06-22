
# Tuim


## Motivation

The project goal is to fly a drone, both piloting and in autonomous flight. However, the project goal is not only to fly a drone, but also to understand the software, hardware, communications, and control systems that make autonomous flight possible.

In order to do so, we will need to explore the technologies that make modern autonomous systems possible. The first technology is the F' framework from NASA [^10]. The reason to chose this framework is that it was proven in more than one project and is open source. We have the opportunity to learn from the same framework that was part of the Ingenuity Mars helicopter [^11]. The second technology is the drone itself. We have chosen to start with a drone simulator and, ideally, a real radio controller. In this way, we can start sooner and cheaper.

The rest of this document gives a few pointers and some findings we have to share from this experience.

## F' Hello Tutorial

To have a first contact with the F', we suggest you to follow the Hello Tutorial [^40], using Github [^41] Codespaces . This experience will let you install software and libraries on a Linux computer, using cloud resources.

We may find other similar frameworks, but we recommend to stay with F' so we can all share a similar experience and help each other.

The idea of using Github Codespaces is that you can run all the tutorial steps from a web browser. You just need to get an account on Github.

Just log in GitHub, create a new repository, select green Code button, and select Codespace tab. You will land on a VS Code running on the cloud, with access to a bash terminal.

Just follow the tutorial instructions to learn about some programming, system administration, components, telemetry, commands, events, and other concepts that are usefull on this kind of system. You will also learn about Linux, git, and GitHub. You can start the tutorial now, if you have internet access and a web browser. 

It may help to imagine what is going on in the tutorial scenario. Imagine a ground control station with a large antena and a rocket on a launch pad.

A command is send to the rocket and the confirmation is sent back from the rocket. The rocket has some values that can be monitored from a distance, telemetry.

```
\|/
-.-                            ||
 |        telemetry            || HiComponent
 |                             ||
/ \                           /__\ 

GDS                           Rocket
```

The Hello Tutorial will take about 2 hours to complete. Explore the code and try Section 6 exercises. Move to the other tutorials, including the LED blinking one.

The tutorial will download the source code of the F', giving the chance of studying the classes that make the component work.

After this introduction on software skills, we can move to some hardware skills.

## Recommended Equipment

To have a first contact with drones, we suggest you to get a Radiomaster Pocket radio controller and log some hours on SkyDive drone simulator. We need to understand drone parts, piloting, and some concepts of flight. This will help us get a deeper understanding of F' and drone in general.

All decisions here were made from the perspective of someone with no previous flight experience and no existing drone equipment. We chose to invest first in a radio controller because it provides practical experience and a better understanding of drone piloting. At the same time, we decided to postpone the decision of whether to buy or build a real drone later on.

To fly a drone, we need two main components: a drone and a radio controller.

A real drone operates on batteries, has a limited flight time, and its operation involves some risk of damage to equipment. A drone simulator, on the other hand, allows us to learn how to pilot a drone without the risk of crashes and without the limitations imposed by battery life.

For these reasons, we decided to start with a simulator rather than a real drone. We chose FPV.SkyDive [^1], a free drone simulator available on Steam.

Later, we may buy or build a real drone. At this stage, however, a simulator provides more benefits for a novice pilot than a physical aircraft.

A radio controller also operates on batteries, but it differs significantly from a gamepad, keyboard, or mouse. While a simulator can be controlled using those devices, doing so would not provide an experience that transfers well to real drone piloting.

Therefore, we decided to purchase a dedicated radio controller. This allows us to learn using the same type of interface employed in real drone operations and preserves the possibility of connecting the controller to a real drone in the future.

We chose the RadioMaster Pocket [^2], an affordable and widely recommended entry-level radio controller for novice pilots. 

You don't need a radio controller, but we can learn a lot about hardware and radio emitters. If you chose not to have a radio controller, you can practice using another controller.

If you chose to have a radio controller, dependending on location you may have to wait some weeks to find a good deal with a local or a online seller. We got our radio conrtoller from an online seller [^3] and the delivey took about two weeks.  

The radio controller came with no batteries included. We bought two batteries from a local seller [^4], after a week locating a seller. The battery model required is flat top, rechargeable, no control chip. This kind of battery is usually available on hobby craft and electronics stores.

Operating hardware brings some safety issues.

## Radio Controller Safety Notes

We are going to operate a radio wave emitter and use a pair of batteries.
Initially, they are the larger safety issues, because we are using a drone simulator.  Because we are using a simulator, we can disable the radio to remove two of the common hazards: (a) radio waves and (b) arming antena. 

Radio waves give the name to radiation, like sun, nuclear, and microwave radiation. Too much radiation can have a nocive effect on living beings. To be safe, we need to limit distance and time of exposition. The main concern is about giving some distance.

The operation with the radio emitter on requires caution.
The controller operator torso must be kept at about 20 cm, like a extended palm, away from the radio controller. The radio controller works emiting radio waves and the manual advises to keep a safe distance following FCC regulations [^20]. Second, the manual warns about damage radio controller if the antena is not extended during operation.

The good news is we can keep the radio emitter off when using a simulator. Data is transfered throug the USB cable, so no need to use the radio.

So, while using the simulator, always check if the radio is disabled and these two radio related hazards are eliminated.

On the other hand, bateries are needed to operate the radio controller, even when we are using a drone simulator. Actually, we have not explored the option of using two separate cables for data and energy at the same time. But we believe the radio controller was designed to be used with batteries on.

Batteries have some hazards and there is a risk of controller damage. A faulty battery can leak acid, blow, or catch fire. Batteries should not stay on the controller if it is not in use for some weeks. It is easy to forget a device stored with batteries in.

During setup, battery polarity can become an issue, because both poles are flat. We found negative pole signs on the battery and the controller case. Turning the radio controller on with the wrong polarity could potentially damage the controller.

Lastly, the controller has a built-in charger, and it is important to not let the batteries charge unattended or near flamable material.

So, now it is time to turn the radio controller on.

## Approaching the Radio Controller

The two most important activities early on are: (a) setup and bind to a drone [^5][^6] and (b) setup and bind to a drone simulator [^7]. We recommend reading some material [^30] and watching some videos before turning the controller on.

The first hours operating a radio controller can be intimidating. There is a lot of concepts for a novice to absorb.

In order to start, we need the radio controller, the USB cable and the two batteries. The cable is a data and charge cable that comes with the radio controller. We tagged this cable to avoid misplacing it or mixing it with other similar cables. We purchased a USB adapter from a local seller, because the cable is USB-A to USB-C. Most computers now use USB-A (the smaller one). We could get a new cable, but the fix is working. This adapter and an A-to-A cable can be found on computer shops.

At any point, if feeling lost. Just use the RTN button to return to the last screen until you are on the first screen. Alternatively, just turn the controller off and on again.

If the controller screen is dimed, move a stick.

Remember to turn the controller off before removing the cable.


## The Very First Session

After reading and watching some instructions, we advise to start small. Just check batteries, turn the radio on and off.

The antena is on top of the controller, along with the USB data port. The batteries holder is on the back, the positive sides are up. We open the compartment cover from the center. A little patience is needed to close it.

The power button is on the front. To turn on or off, we need to press it for more than one second. If the button turns green, the controller is on.

A warning is common at this point, because it is expected that controls are in a safe position when we turn it on. It will make sense with practice, throttle control and switches must be off so we do not send a real drone flying too soon. 

## Creating a Simulator Configuration

Turn the controller on. On right side, press MDL round button. Move the wheel on the right to 02 FPV DRONE. Press the wheel, select Copy model. Just move the wheel and press the wheel again. You may get 05 FPV DRONE, a copy of the original model.

From now on, select this model when using the simulator. Use the wheel to select the model. Selected model has a star (*). You should be looking at * 05 FPV DRONE.

Make sure the radio is off on this model. Hold the power button, turn off the controller. Hold the power button again, Press MDL and the select model should be the new 05 FPV DRONE.

On the left side column, press the PAGE button until you are on SETUP 2/12. Now use the wheel to look for Internal RF and External RF as Mode OFF. 

Disabling the radio avoids RF transmission,  during simulator use, reduces battery consumption, and eliminates concerns related to antenna deployment.

## Setting Date and Time

The controller has an internal clock. We can set it up to have a reliable clock.
Press SYS, then press PAGE twice to get RADIO SETUP 3/7. Use the wheel to select date or time item to adjust. 

From this point on, date and time are precise and the model is set to disable radio.

## Playing Games

We suggest you use some games to get a hold of what the controllers do. My favorite game is X-tris.

To select a game, press SYS, then use the wheel to select you game. Sticks are sensitive, just go slow and have patience.

## Connecting as a Battery Charger

Turn the computer on, connect the USB cable on the computer. Connect the other side on the bottom USB port. Turn the controller on.

You should see a light inside the controller. After a few minutes, the battery voltage indicator should go higher. The battery is charging. 

Using a simulator, the battery lasts much longer than when flying a real drone with the radio on.


## Connecting as a Human Interface Device

USB HID top port


## Drone Simulator


Connect USB cable to computer



Connect USB cable on upper port

Play INTRO

## A First Telemetry Source


F' telemetry allow us to get readings from distance. We need an object or a source to be measured, usually a kind of vehicle: a rocket, a rover, a drone, or a satellite.

Usually, the readings are confirmation of commands, position and values from sensors. We don't need a complex and expensive vehicle to have a first experience, currently, a smartphone has a set of sensors.

Our first code is a simple web page that collects the GPS position on the web browser client hardware. This first prototype has no relation with F', but allow us to learn about the kind of reading that we are trying to get from a distance.

A real drone could be a more realistic source, but a smartphone is a common item and any computer with a web browser could be used to collect readings.


## A F' Prime Bridge to the Web World

We need a way to connect the reading from smartphone with a F' component, similar to the Hi Component from the Hello Tutorial.  

```
\|/
-.-                            
 |        telemetry      | HiComponent | | Bridge |        | Tuim |
 |                             
/ \                           

GDS                                 Web server             Web browser
```

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
[^41]: https://github.com