![image](https://user-images.githubusercontent.com/90430427/133154198-7da21197-0acb-43ac-8155-4d1edbcf3f02.png)

# grungegirl. cli-based drug search for girls.

welcome.

`grungegirl` is aiming to be the premier drug culture application. it is the hacker's encyclopedia for drugs, programmed by a hardcore feminist who is struggling with themes of oppression in drug culture. drugs and their addicts are treated unfairly, even by people who are meant to support them. they are also viewed as lesser by society, even though many of them are smarter and better.

`grungegirl` is built to break the rules. mentioning its purpose as an application gets the conversation started, and the moral high horses come out to play. 

this is the swiss army knife for those interested in drug culture. it is not built to enable users, as this application has very little choice over whether or not that person becomes a drug addict after using it.

it is instead built to level the playing field, giving people who are often ignored by society tools that help them explore and conquer the world of drugs. drugs can destroy lives, but so can everything else. we shouldn't hurt those that choose to indulge in them. 

![image](https://user-images.githubusercontent.com/90430427/133360635-6154db5b-5693-4914-841e-ba87523ddde7.png)

to install it, run the `install.py` file. 
the `install.py` file will install `browsh`, move necessities to a folder in `$HOME` and bind a command. 
in the future, it will also attempt to compile `browsh` from source or otherwise install it cleanly in distros where it can get away with it.

## why was this even bothered with. idiot.

like i said, drug addicts are treated very poorly throughout history. it's time to have a small win within the community, making an application that adds movement to that lifestyle. drugs can benefit from a bit of organization, anyway. there's nothing cooler to me right now other than being able to understand quick info about drugs in a heartbeat. 

it's something i've needed for a while, but never knew how to bring into existence until now. as an addict myself, i've been told the idea is "life-saving" by people within the drug community. that is how i know i'm on to something. people who could really use a utility like this are aware of how badly they've needed it. it's become subconscious in the mind of a drug addict to always be worth bones.

but with bones comes fertilization, and it is time for this soil to grow something mutated and new. it feels cool to be apart of a neglected community if you're helping them. 

## explaining the spider leg file theory

for now, just trust me. the spider-leg layout is a decision emphasizing the modular aspect of python code and extending the capabilities of the software. i notice that this layout folds in and out like an umbrella on a system due to install/uninstall pathing. it made the use of `lynx` possible through its "jumping-spider" style import installation. 

it's modularity will come in handy when i give the lynx integration its final polish around 0.6.0. folders will be applied to different sections. 
the only other option is to have a few files that are just fucking huge and annoying to work through when wanting to make quick changes. the files also won't be able to borrow content from one another in order to mix and match information.

![image](https://user-images.githubusercontent.com/90430427/133361279-919c0133-e847-4602-ac44-0620a868b8bb.png)


the spider provides a strong idea for maintaining modularity in my code. each leg is a modicum of a larger scale project that needs each leg to work. without the legs, nothing moves. the body is made of files like `install.py`, `uninstall.py` and `query.py`. These three files are the head and torso of the spider, bringing motor functionality to the legs. that now means each leg can be upgraded individually without affecting the rest of the body. this will make updating information very easy in the future.

the only downside is that i need to open lots of files to make huge updates to layout and formatting. that's for me to worry about though, and affects no part of the user experience.


## planned updates. cycles for the future.

- Massive repository of drugs organized by category, class, price and legality.
- Overwhelming breadth of information related to astrology, accessible offline and fast.
- Onion Link/Tor Browser Redirect, Sellers, Marketplaces, Amazon. Editable through Python coding to launch a browser of your choice.
- Information available on how to securely use Tor and the rest of the internet.

- `crypto` command for monitoring cryptocurrency prices and managing a wallet.
- `buy` will open a list of products that you can access online in a browser of your choosing.
- `rehab` will use approximate location to find and target rehabs in your area.
- `reports` will display trip reports based on whatever drug you request to hear them about.


![image](https://user-images.githubusercontent.com/90430427/133165416-e009fb21-b4ca-46e4-b3d2-1b61543a1a41.png)

## included functions. humble beginnings.

- `web` opens the ability to search psychonaut.wiki for more information related to the available list of drugs. 

- `exit` will formally exit the application. you could also just spam ctrl + c.

![image](https://user-images.githubusercontent.com/90430427/133362528-8c613e06-56f8-40bf-b2fc-4b01bce7d19a.png)
