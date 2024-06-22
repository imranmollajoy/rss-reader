Anne Aaron just can’t help herself.

Aaron, Netflix’s senior encoding technology director, was watching the company’s [livestream of the Screen Actors Guild Awards](/2023/1/11/23550215/netflix-sag-awards-livestreaming-youtube) earlier this year. And while the rest of the world marveled at all those celebrities and their glitzy outfits sparkling in a sea of flashing cameras, Aaron’s mind immediately started to analyze all the associated visual challenges Netflix’s encoding tech would have to tackle. “Oh my gosh, this content is going to be so hard to encode,” she recalled thinking when I recently interviewed her in Netflix’s office in Los Gatos, California.

Aaron has spent the past 13 years optimizing the way Netflix encodes its movies and TV shows. The work she and her team have done allows the company to deliver better-looking streams over slower connections and has resulted in 50 percent bandwidth savings for 4K streams alone, according to Aaron. Netflix’s encoding team has also contributed to industrywide efforts to improve streaming, [including the development of the AV1 video codec](/2021/11/10/22775150/netflix-av1-codec-tv-streaming-ps4-pro) and its eventual successor.

Now, Aaron is getting ready to tackle what’s next for Netflix: Not content with just being a service for binge-watching, the company ventured into [cloud gaming](/2023/11/13/23958926/netflix-cloud-gaming-tv-games-leanne-loombe-interview) and [livestreaming](/2022/11/10/23451880/netflix-chris-rock-comedy-live-special-2023) last year. So far, Netflix has primarily dabbled in one-off live events like the SAG Awards. But starting next year, the company will stream WWE RAW live every Monday. The streamer [nabbed the wrestling franchise from Comcast’s USA Network](/2024/1/23/24047785/netflix-monday-night-raw-exclusive-live-streaming-leaving-cable), where it has long been the No. 1 rated show, regularly drawing audiences of [around 1.7 million viewers](https://variety.com/2024/tv/news/wwe-ratings-smackdown-raw-nxt-1235956750/). Satisfying that audience week after week poses some very novel challenges.

“It’s a completely different encoding pipeline than what we’ve had for VOD,” Aaron said, using industry shorthand for on-demand video streaming. “My challenge to (my) team is to get to the same bandwidth requirements as VOD but do it in a faster, real-time way.”

To achieve that, Aaron and her team have to basically start all over and disregard almost everything they’ve learned during more than a decade of optimizing Netflix’s streams — a decade during which Netflix’s video engineers re-encoded the company’s entire catalog multiple times, began using machine learning to make sure Netflix’s streams look good, and were forced to tweak their approach when a show like *Barbie Dreamhouse Adventures* tripped up the company’s encoders.

------------------------------------------------------------------------

When Aaron joined Netflix in 2011, the company was approaching streaming much like everyone else in the online video industry. “We have to support a huge variety of devices,” said Aaron. “Really old TVs, new TVs, mobile devices, set top boxes: each of those devices can have different bandwidth requirements.”

To address those needs, Netflix encoded each video with a bunch of different bitrates and resolutions according to a predefined list of encoding parameters, or recipes, as Aaron and her colleagues like to call them. Back in those days, a viewer on a very slow connection would automatically get a 240p stream with a bitrate of 235 kbps. Faster connections would receive a 1750 kbps 720p video; Netflix’s streaming quality topped out at 1080p with a 5800 kbps bitrate. 

The company’s content delivery servers would automatically choose the best version for each viewer based on their device and broadband speeds and adjust the streaming quality on the fly to account for network slow-downs.

To Aaron and her eagle-eyed awareness of encoding challenges, that approach seemed inadequate. Why spend the same bandwidth to stream something as visually complex as an action movie with car chases (lots of motion) and explosions (flashing lights and all that noisy smoke) as much simpler visual fare? “You need less bits for animation,” explained Aaron. 

*My Little Pony,* which was a hit on the service at the time, simply didn’t have the same visual complexity as live-action titles. It didn’t make sense to use the same encoding recipes for both. That’s why, in 2015, Netflix began re-encoding its entire catalog with settings fine-tuned per title. With this new, title-specific approach, animated fare could be streamed in 1080p with as little as 1.5 Mbps.

*She-Ra and the Princess of Power* is another good example of an animated show with fairly simple visual complexity versus live action-fare.

Image: Netflix

Switching to per-title encoding resulted in bandwidth savings of around 20 percent on average — enough to make a notable difference for consumers in North America and Europe, but even more important as Netflix was eyeing its next chapter: in January of 2016, [then-CEO Reed Hastings announced](/2016/1/6/10724112/netflix-global-expansion-russia-india) that the company was expanding into almost every country around the world — including markets with subpar broadband infrastructure and consumers who primarily accessed the internet from their mobile phone.

Per-title encoding has since been adopted by most commercial video technology vendors, [including Amazon’s AWS](https://aws.amazon.com/blogs/media/introducing-automated-abr-adaptive-bit-rate-configuration-a-better-way-to-encode-vod-content-using-aws-elemental-mediaconvert/), which used the approach [to optimize](https://aws.amazon.com/blogs/media/pbs-modernizes-its-video-encoding-workflow-with-aws-elemental-mediaconvert/) PBS’s video library last year. But while the company’s encoding strategy has been [wholeheartedly endorsed](https://streaminglearningcenter.com/encoding/how-netflix-pioneered-per-title-video-encoding-optimization.html) by streaming tech experts, it has been largely met with silence by Hollywood’s creative class.

Directors and actors like Judd Apatow and Aaron Paul [were up in arms](/2019/10/29/20937546/netflix-playback-speed-testing-android-mobile-tv-movies-hollywood-filmmakers) when Netflix began to let people change the playback speed of its videos in 2019. Changes to the way it encodes videos, on the other hand, never made the same kinds of headlines. That may be because encoding algorithms are a bit too geeky for that crowd, but there’s also a simpler explanation: the new encoding scheme was so successful at saving bandwidth without compromising on visual fidelity that no one noticed the difference. 

------------------------------------------------------------------------

Make that almost no one: Aaron quickly realized that the company’s per-title-based encoding approach wasn’t without faults. One problem became apparent to her while watching *Barbie Dreamhouse Adventures*. It’s one of those animated Netflix shows that was supposed to benefit the most from a per-title approach. 

However, [Netflix’s new encoding struggled with one particular scene](https://go.skimresources.com/?id=1025X1701640&xs=1&url=https%3A%2F%2Fwww.netflix.com%2Fwatch%2F80009402%3FtrackId%3D14277283%26tctx%3D-97%252C-97%252C%252C%252C%252C%252C%252C%252C70294800%252CVideo%253A80009402%252CdetailsPageEpisodePlayButton). “There’s this guy with a very sparkly suit and a sparkly water fountain behind him,” said Aaron. The scene looked pretty terrible with the new encoding rules, which made her realize that they needed to be more flexible. “At (other) parts of the title, you need less bits,” Aaron said. “But for this, you need to increase it.”

That’s a lot of glitter to properly encode.

Screenshot: Netflix

The solution to this problem was to get a lot more granular during the encoding process. Netflix began to break down videos by shots and apply different encoding settings to each individual segment in 2018. Two people talking in front of a plain white wall were encoded with lower bit rates than the same two people taking part in a car chase; Barbie hanging out with her friends at home required less data than the scene in which Mr. Sparklesuit shows up.

As Netflix adopted 4K and HDR, those differences became even more stark. “(In) *The Crown*, there’s an episode where it’s very smokey,” said Aaron. “There’s a lot of pollution. Those scenes are really hard to encode.” In other words: they require more data to look good, especially when shown on a big 4K TV in HDR, than less visually complex fare.

------------------------------------------------------------------------

Aaron’s mind never stops looking for those kinds of visual challenges, no matter whether she watches Netflix after work or goes outside to take a walk. This has even caught on with her kids, with Aaron telling me that they occasionally point at things in the real world and shout: “Look, it’s a blur!”

It’s a habit that comes with the job and a bit of a curse, too — one of those things you just can’t turn off. During our conversation, she picked up her phone, only to pause and point at the rhinestone-bedazzled phone case. It reminded her of that hard-to-encode scene from *Barbie Dreamhouse Adventures*. Another visual challenge!

Still, even an obsessive mind can only get you so far. For one thing, Aaron can’t possibly watch thousands of Netflix videos and decide which encoding settings to apply to every single shot. Instead, her team compiled a few dozen short clips sourced from a variety of shows and movies on Netflix and encoded each clip with a range of different settings. They then let test subjects watch those clips and grade the visual imperfections from not noticeable to very annoying. “You have to do subjective testing,” Aaron said. “It’s all based on ground truth, subjective testing.”

London’s smoggy fog of the early 50s in *The Crown* made for another encoding challenge.

Screenshot: Netflix

The insights gained this way have been used by Netflix to train a machine learning model that can analyze the video quality of different encoding settings across the company’s entire catalog, which helps to figure out the optimal settings for each and every little slice of a show or movie. The company collaborated with the University of Southern California on developing these video quality assessment algorithms and [open-sourced](https://github.com/Netflix/vmaf) them in 2016. Since then, it has been adopted by much of the industry as a way to analyze streaming video quality and even [gained Netflix an Emmy Award](https://www.linkedin.com/posts/anne-aaron_vmaf-wearenetflix-activity-6851698008405499904-_SHa/?trk=public_profile_like_view). All the while, Aaron and her team have worked to catch up with Netflix’s evolving needs — like HDR. 

“We had to develop yet another metric to measure the video quality for HDR,” Aaron said. “We had to run subjective tests and redo that work specifically for HDR.” This eventually allowed Netflix to encode HDR titles with per-shot-specific settings as well, which the company finally did last year. Now, her team is working on open-sourcing HDR-based video quality assessment.

------------------------------------------------------------------------

Slicing up a movie by shot and then encoding every slice individually to make sure it looks great while also saving as much bandwidth as possible: all of this work happens independently of the video codecs Netflix uses to encode and compress these files. It’s kind of like how you might change the resolution or colors of a picture in Photoshop before deciding whether to save it as a JPEG or a PNG. However, Netflix’s video engineers have also actively been working on advancing video codecs to further optimize the company’s streams.

Netflix is a founding member of the [Alliance for Open Media](https://aomedia.org/), whose other members include companies like Google, Intel, and Microsoft. Aaron sits on the board of the nonprofit, which has spearheaded the development of the open, royalty-free AV1 video codec. Netflix began streaming some videos in AV1 [to Android phones in early 2020](/2020/2/6/21126039/netflix-android-av1-video-codec-efficient-support-bandwidth-quality-vp9) and has since expanded to [select smart TVs and streaming devices](/2021/11/10/22775150/netflix-av1-codec-tv-streaming-ps4-pro) as well as iPhones. “We’ve encoded about two-thirds of our catalog in AV1,” Aaron said. The percentage of streaming hours transmitted in AV1 is “in the double digits,” she added.

And while the roll-out of AV1 continues, work is already underway on its successor. It might take a few more years before devices actually support that next-gen codec, but [early results suggest](https://go.skimresources.com/?id=1025X1701640&xs=1&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdjxlRoyNQ8g%26t%3D998s) that it will make a difference. “At this point, we see close to 30 percent bit rate reduction with the same quality compared to AV1,” Aaron explained. “I think that’s very, very promising.”

*Meridian* was a short film made by Netflix specifically to test and train codecs and algorithms for streaming.

Screenshot: Netflix

While contributing to the development of new video codecs, Aaron and her team stumbled across another pitfall: video engineers across the industry have been relying on a relatively small corpus of freely available video clips to train and test their codecs and algorithms, and most of those clips didn’t look at all like your typical Netflix show. “The content that they were using that was open was not really tailored to the type of content we were streaming,” recalled Aaron. “So, we created content specifically for testing in the industry.”

In 2016, [Netflix released](https://variety.com/2016/digital/news/netflix-meridian-imf-tools-open-source-1201859416/) a 12-minute 4K HDR short film called [*Meridian*](https://go.skimresources.com/?id=1025X1701640&xs=1&url=https%3A%2F%2Fwww.netflix.com%2Ftitle%2F80141336) that was supposed to remedy this. *Meridian* looks like a film noir crime story, complete with shots in a dusty office with a fan in the background, a cloudy beach scene with glistening water, and a dark dream sequence that’s full of contrasts. Each of these shots has been crafted for video encoding challenges, and the entire film has been released under a Creative Commons license. The film has since been used [by the Fraunhofer Institute](https://www2.iis.fraunhofer.de/AAC/xhe-aac-compare-tab.html) [and](https://streaminglearningcenter.com/ffmpeg/maximizing-quality-and-throughput-in-ffmpeg-scaling.html) [others](https://www.frontiersin.org/articles/10.3389/frsip.2022.885644/full) to evaluate codecs, and its release has been [hailed](https://creativecommons.org/2016/09/16/netflix-releases-meridian-creative-commons/) by the Creative Commons foundation as a prime example of “a spirit of cooperation that creates better technical standards.”

------------------------------------------------------------------------

Cutting-edge encoding strategies, novel quality metrics, custom-produced video assets, and advanced codecs: in many ways, Netflix has been leading the industry when it comes to delivering the best-looking streams in the most efficient ways to consumers. That’s why the past 14 months have been especially humbling.

Netflix launched its very first livestream in March of 2023, [successfully](https://www.tvrev.com/news/netflix-gets-its-live-hit-cultural-moment-with-chris-rocks-revenge) broadcasting a Chris Rock comedy special to its subscribers. A month later, it tried again with a live reunion event for its reality show *Love Is Blind* — and [failed miserably](/2023/4/16/23685828/netflix-love-is-blind-reunion-live-delay-problems), with viewers waiting for over an hour for the show to start.

The failed livestream was especially embarrassing because it tarnished the image of Netflix as a technology powerhouse that is lightyears ahead of its competition. Netflix co-CEO Greg Peters issued a rare mea culpa later that month. “We’re really sorry to have disappointed so many people,” Peters [told investors](https://s22.q4cdn.com/959853165/files/doc_financials/2023/q1/netflix-inc-q1-2023-pre-recorded-earnings-call-apr-18-2023.pdf). “We didn’t meet the standard that we expect of ourselves to serve our members.”

Netflix wants to avoid further such failures, which is why the company is playing it safe and moving slowly to optimize encoding for live content. “We’re quite early into livestreaming,” Aaron said. “For now, the main goals are stability, resilience of the system, and being able to handle the scale of Netflix.” In practice, this means that Aaron’s team isn’t really tweaking encoding settings for those livestreams at all for the time being, even if it forces her to sit through the livestream of the SAG Awards show without being able to improve anything. “We’re starting with a bit more industry-standard ways to do it,” she told me. “And then from there, we’ll optimize.”

The same is true in many ways for cloud gaming. [Netflix began to test](https://about.netflix.com/en/news/testing-games-on-more-devices) games on TVs and desktop computers last summer and has since slowly expanded those efforts to include additional markets and titles. With games being rendered in the cloud as opposed to on-device, cloud gaming is essentially a specialized form of livestreaming, apart from one crucial distinction. “They’re quite different,” said Aaron. “\[With\] cloud gaming, your latency is even more stringent than live.” 

Monday Night RAW is coming to Netflix next year and will bring with it even more opportunities to challenge the streamer’s video encoding technology.

Photo: WWE/Getty Images

Aaron’s team is currently puzzling over different approaches to both problems, which requires them to ignore much of what they’ve learned over the past decade. “The lesson is not to think about it like VOD,” Aaron said. One example: slicing and dicing a video by shot and then applying the optimal encoding setting for every shot is a lot more difficult when you don’t know what happens next. “With live, it’s even harder to anticipate complex scenes,” she said.

Live is unpredictable: that’s not just true for encoding but also for Netflix’s business. The company just inked a deal to show [two NFL games on Christmas Day](/2024/5/15/24157289/netflix-nfl-game-streaming-global-christmas-day) and will begin streaming weekly WWE matches in January. This happens as sports as a whole, which has long been the last bastion of cable TV, is transitioning to streaming. [Apple is showing MLS games](/2022/6/14/23167555/apple-tv-mls-live-sports-streaming), Amazon is [throwing tons of money at sports](https://www.axios.com/2024/05/19/amazon-nba-deal-nfl), and ESPN, Fox, and Warner Bros. are banding together to launch [their own sports streaming service](/2024/5/16/24158201/venu-sports-streaming-service-espn-fox-warner-bros). Keeping up with these competitors doesn’t just require Netflix to spend heavily on sports rights but also actually get good at livestreaming. 

All of this means that Aaron and her team won’t be out of work any time soon — especially since the next challenge is always just around the corner. “There’s going to be more live events. There’s going to be, maybe, 8K, at some point,” she said. “There’s all these other experiences that would need more bandwidth.”

In light of all of those challenges, does Aaron ever fear running out of ways to optimize videos? In other words: how many times can Netflix re-encode its entire catalog with yet another novel encoding strategy, or new codec, before those efforts are poised to hit a wall and won’t make much of a difference anymore?

“In the codec space, people were saying that 20 years ago,” Aaron said. “In spite of that, we still find areas for improvement. So, I’m hopeful.”

And always eagle-eyed to spot the next visual challenge, whether it’s a sea of camera flashes or a surprise appearance by Mr. Sparklesuit.
