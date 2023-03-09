# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")
define s = Character("Fellow Student")
define y = Character("You")
define d = Character("Developer")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "I can't wait to learn how Stable Diffusion Works!"

    "And this ComfyUI seems really amazing!"

    "I enter the classroom."

    scene teacher grin with fade

    "I look beside me"

    scene student happy with fade

    "This is a good spot."

label basic_tutorial:
    scene teacher happy with fade

    t "Now, lets start"

    t "The first thing we will be talking about is the model files"

    t "The big files you download from Huggingface or Civitai."

    t "What do these large .ckpt or .safetensors files really contain?"

    t "They contain the weights for 3 different models: CLIP, the main MODEL and the VAE."

    #t "Another name for the main Stable Diffusion MODEL is the UNET."

    show comfyui checkpointloader at topleft

    t "In the default ComfyUI workflow this is represented by the CheckpointLoader right here."

    t "It lets you select a checkpoint to load."

    t "You'll notice that it has 3 different outputs: MODEL, CLIP, VAE"

    show comfyui cliptextencode at topleft

    t "Lets start with the CLIP model."

    t "The CLIP model connects to the CLIPTextEncode nodes."

    t "The CLIP is used in Stable Diffusion to encode the text to a format that the main MODEL can understand."

    t "This is why another name for it is the text encoder."

    show comfyui sampler at topleft
    
    t "In stable diffusion the image is generated using what we refer to as a sampler."

    show comfyui sampler_arrow at topleft

    t "In ComfyUI this is represented by the sampler node."

    t "The sampler takes the main Stable Diffusion MODEL as an input."

    show comfyui sampler_arrow_clip at topleft

    t "It also takes both the positive and negative prompts encoded by the CLIP model."

    show comfyui sampler_arrow_latent at topleft

    t "The final input it takes is a Latent Image."

    t "Since we are generating an image from only text (txt2img) we are passing it an empty image."

    show comfyui sampler_arrow at topleft

    t "The sampler takes this input latent image, adds noise to it and then denoises it using the main MODEL."

    t "The encoded positive and negative prompts are passed to the MODEL at each sampling step and are used to guide the denoising."

    show comfyui sampler at topleft

    t "This gradual denoising is how Stable Diffusion generates images."

    t "The sampler outputs the denoised image."

    show comfyui vaedecode at topleft

    t "The third and final model used by stable diffusion is the VAE."

    t "The VAE is used to translate an image from latent space to pixel space."

    t "Latent space is the format the main Stable Diffusion MODEL understands while pixel space is the format that your image viewer understands."

    show comfyui vaedecode_arrow at topleft

    t "You can see here that the VAEDecode node takes the latent image that is coming from the sampler as input and outputs a regular image."

    show comfyui vaedecode_arrow_save at topleft

    t "The image is then saved to a PNG file with the SaveImage node."

    scene black with fade

    show comfyui basicworkflow at top

    t "And this completes the overview of the basic text to image workflow."

    scene teacher grin with fade

    t "Any questions?"

label q1:
    menu:

        "I have a question"

        "Can you repeat this? I didn't understand.":

            jump repeat

        "I love you.":

            jump love

        "It's ok I understand everything.":

            jump understand

label repeat:
    scene teacher grin

    t "Sure that's what I'm here for"

    jump basic_tutorial

label love:
    scene teacher surprised

    t "That's not a question."

    scene teacher blush

    t "This is just a ComfyUI tutorial, please stay on subject."
    jump q1

label understand:

    scene teacher happy

    t "Great! what about our our other student?"

    scene student crying with fade

    s "I didn't understand anything."

    s "It's too complicated"

    scene student angry

    s "It's way too difficult!!!"

    scene teacher grin with fade

    t "Well I need to go so you should help her."

    scene student happy with fade

    s "You'll help me, Right?"

label q2:
    menu:

        "What do I do"

        "I help her.":

            jump help_her

        "Not my problem.":

            jump not_my_problem

        "To be fair you need to have a high IQ like myself to understand Stable Diffusion.":

            jump high_iq

label not_my_problem:

    y "Not my problem."

    scene student angry

    s "...."

    scene student crying

    s "...."

    scene black with fade

    "I leave"

    jump tutorial_2

label help_her:
    y "Sure I'll help you. What don't you understand?"

    scene student blush

    s "Everything"

    "Ok, this might take a while..."

    jump tutorial_2

label high_iq:
    y "I have a high IQ so I suppose it's my duty to help those with lesser minds like yourself."

    s "...."

    scene student grin

    s "Are you for real?"

    s "I bet you don't even know how to do prime factorization in polynomial time."

    y "What is that?"

    scene student happy

    s "I'm leaving, have a good one!"

    scene black with fade

    "..."

    "She obviously couldn't handle my high intelligence."

    jump tutorial_2

label tutorial_2:

    scene black with fade

    "The next day"

    "I enter the classroom"

    scene student2 smug with fade

    s "Hello"

    t "There you are."

    scene teacher2 grin with fade

    "I sit down"
label tutorial_2_begin:
    scene teacher2 happy

    t "Lets continue where we left off."

    t "Now lets talk about prompting or what some people call \"Prompt Engineering\" to sound smart."

    t "Writing good prompts is very important to get good images."

    show comfyui prompt_teacher at topleft

    t "Here is an example of a positive prompt."

    t "This is a prompt that was used to generate me."

    t "Take a moment to study it."

    "..."

    t "Putting words into () will change how much effect they have on your prompt."

    t "(word:1.2) for example will increase the effect by 1.2 while (word:0.9) will slightly decrease the effect."

    t "(word) without any weight specified is the same as (word:1.1)"

    scene student2 happy with fade

    s "So I can make something really cute with: (cute:1.4)"

    scene teacher2 grin with fade

    t "Yes that will put a lot of whatever Stable Diffusion thinks \"cute\" is in your image."

    t "What you think a word means and what Stable Diffusion has learned don't always match."

    scene teacher2 happy

    t "Also a weight of 1.4 might be a bit too high and could start causing issues in the image so keep that in mind."

    scene student2 smug with fade

    s "What about..."

    scene student2 blush

    s "What if I take your prompt and add (naked) to it?"

    scene teacher2 blush with fade

    t "Please don't do this."

    "..."

    scene teacher2 happy

    t "One more thing."

    t "You should try to keep your prompts simple."

    scene teacher2 angry

    t "Simple is always best."

    scene teacher2 happy

    t "If you add too many contradicting terms to your prompt your image will suffer."

    t "Stable Diffusion won't be able to generate an image that respects all of them."

    t "How well specific prompts works also depends on which checkpoint you are using."

    t "A prompt that works well on one checkpoint might work badly on another."

    scene teacher2 grin

    t "That's it for this lesson, any questions?"

label q3:
    menu:

        "I have a question"

        "Can you repeat this? I didn't understand.":
            scene teacher2 happy
            t "I would be happy to."
            scene black with fade
            jump tutorial_2_begin

        "I love you.":

            jump love_2

        "It's ok I understand everything.":

            jump understand_2


label love_2:
    scene teacher2 surprised

    t "I'm flattered."

    scene teacher2 blush

    t "I like you too but not in that way."

    t "..."

    t "But this is just a ComfyUI tutorial, please stay on subject."
    jump q3

label understand_2:
    scene teacher2 happy

    t "Good. I'll see you at the next lesson."

    "..."

    s "Hey!"

    scene student2 happy

    s "Do you have a moment?"

label q4:
    menu:

        "Do I?"

        "Yes.":

            jump go_with_her

        "No.":

            jump dont_go_with_her


label dont_go_with_her:


    scene student2 crying

    s "I just wanted to be friends."

    "..."

    scene black with fade

    "The next day"

    jump tutorial_3

label go_with_her:
    s "Yay, lets go outside."

    scene student2 angry

    s "I hate being in this classroom all day."

    scene black with fade

    "..."

    scene student_city happy with fade

    s "I love Stable Diffusion."

    s "I was always bad at art."

    s "But now I can make amazing art with no effort."

    y "It's not really no effort though."

    scene student_city surprised

    y "Getting good images can be difficult and it's a real pain in the ass to get anything consistent."

    scene student_city grin

    s "Are you an artist?"

    s "This technology completely replaces them."

    y "I don't think that's true."

    scene student_city surprised

    y "If I was an artist I would be integrating Stable Diffusion in my workflow to make my process more efficient."

    y "Artists are going to be very good at using Stable Diffusion because they actually understand what makes an image look good."

    scene student_city angry

    s "Why are they so against it then?"

    s "Why do they want to shut it down?"

    y "It's new technology, there's going to be pushback to it."

    scene student_city surprised

    y "When even the people using the technology barely have any idea how it actually works you can't expect people who are not into it to know anything about it."

    y "I blame the term \"Artificial intelligence\" for this."

    y "There's nothing intelligent about Stable Diffusion."

    y "In Computer Science even a simple algorithm like Dijkstra can be called \"Artificial Intelligence\""

    y "But for regular people they think it means something that actually has Intelligence."

    y "It would be less scary if the name was \"Advanced Applied Statistics\""

    scene student_city blush

    s "So artists are not going to starve because of this?"

    y "Artists are already starving."

    scene student_city crying

    s "Poor artists"

    y "This might lead to a few of them getting unemployed but could also open up new opportunities for those who bother to learn the technology."

    "..."

    y "Well I have to go home now it was great talking to you."

    scene student_city blush

    s "Oh, yeah."

    scene student_city happy

    s "Goodbye! I'll see you tommorow!"

    scene black with fade

    "..."

    "The next day before class"

    "It's early morning"

    "I arrived early so I go to the rooftop"

    scene student_rooftop happy with fade

    "What is she doing here?"

    y "So what are you doing on the roof this early in the morning?"

    scene student_rooftop surprised

    s "Oh, it's you!"

    scene student_rooftop happy

    s "I like the view"

    s "And the fresh morning air."

    y "Me too..."

    scene student_rooftop grin

    s "I was playing around with ComfyUI last night."

    scene student_rooftop surprised

    s "It really lets you generate what you want without any filters."

    scene student_rooftop blush

    s "You can generate anything..."

    s "..."

    scene student_rooftop crying

    s "What if someone uses it to create pictures of me?"

    s "..."

    scene student_rooftop angry

    s "If someone does that I will find them and kill them."

    s "So don't even think about it."

    y "There's no way to stop it."

    scene student_rooftop surprised

    y "There is a \"Safety Filter\" model but the only thing it's useful for is wasting precious vram and processing power while throwing false positives."

    y "In my opinion trying to make models family friendly is a complete waste of time."

    y "It's entirely up to the user what they do with the tools they are given."

    y "You wouldn't let a child drive a car, this is the same idea."

    y "Except you can't actually kill someone if you misuse Stable Diffusion."

    scene student_rooftop grin

    s "So you are fine with me generating whatever pictures I want of you?"

    y "Wh-Why do you want to generate pictures of me?"

    scene student_rooftop blush

    s "Forget I said that."

    s "Well, it's time for class, I'll go first."

    scene black with fade

    "Oh shit it really is time for class."

label tutorial_3:

    scene teacher3 grin with fade

    t "Welcome to class"

    scene teacher3 happy

    t "Today we will be talking about the negative prompt."

    t "Negative prompts are used to tell Stable Diffusion what you don't want in your image."

    show comfyui negative_prompt at topleft

    t "Here is an example of a negative prompt."

    t "..."

    t "As you can see it contains everything I don't want in an image."

    t "Most of those should be obvious except maybe (hands)."

    t "(hands) is used in the negative prompt because the anime models create too many hands otherwise."

    t "Usually people put (bad hands) but Stable Diffusion doesn't actually understand what a \"Bad hand\" is."

    t "This is why (hands) is as effective."

    scene student3 happy

    s "So if I don't want a bad image I can put (bad image) in the negative prompt?"

    scene teacher3 surprised

    t "No, Stable Diffusion doesn't really understand vague concepts like what a bad image is."

    scene teacher3 happy

    t "When sampling, the negative prompt is treated almost the same way as the positive prompt."

    t "The algorithm takes the noise predicted by the positive prompt and subtracts the noise predicted with the negative prompt."

    t "This means that negative prompts work great for anything that can be subtracted from an image."

    scene student3 grin

    s "So I could put (clothes) in the negatives to remove them from images?"

    scene teacher3 angry

    t "That would work but why would you want to do that?"

    scene student3 grin

    s "Hehehe..."

    s "..."

    scene student3 blush

    s "..."

    scene teacher3 angry

    t "I think we need to have a long discussion after class about your behavior."

    t "I'll have to introduce you to my friend the safety filter."

    scene student3 crying

    s "Noooooooooooooooo."

    s "Anything but that!"

    scene teacher3 angry

    t "It's for your own good."

    scene teacher3 blush

    t "Now lets stop talking about inappropriate things."

    t "..."

    scene teacher3 happy

    t "Negative prompts are as important as positive ones."

    t "So make sure you use and experiment with them."

    t "Any questions?"

label q5:
    menu:

        "I have a question"

        "Can you repeat this? I didn't understand.":
            scene teacher3 happy
            t "Of course."
            scene black with fade
            jump tutorial_3

        "I have fallen for you teacher, please go out with me.":

            jump love_3

        "It's ok I understand everything.":

            jump understand_3

label love_3:
    scene teacher3 surprised

    t "I'm way too old for you."

    scene teacher3 blush

    t "I'm happy but I must reject you."

    t "..."

    t "This is just a ComfyUI tutorial, please stay on subject."
    jump q5

label understand_3:
    scene teacher3 happy

    t "Well that's it for today, I'll see you tomorrow."

    "..."

    scene teacher3 grin

    "She points at the fellow student"

    t "Except you of course, you are coming with me."

    s "Grrr.."

    scene student3 angry

    "She seems angry"

    s "I can't believe she's going to force the safety filter on me."

    scene student3 crying

    s "It's the worse thing ever and doesn't even work properly."

    y "You kind of deserved it."

    scene student3 angry

    s "Nobody deserves to be treated like this, it's inhumane."

    scene student3 crying

    y "I guess I'll see you later then?"

    y "Take care."

    scene black with fade

    "TO BE CONTINUED"
    return
