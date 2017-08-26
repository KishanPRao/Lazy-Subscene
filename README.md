# Lazy-Subscene
A Python script to download movie subtitles from Subscene (subscene.com)

### Usage:
python Lazy-Subscene.py "file-name"

Other options can be included, such as: <br/>
-dir->For directory operations. fsub->Place both subtitles & the file in a separate folder. sub->Place the subtitles in a separate folder. <br/>
-hi->Search for Hearing Impaired subtitles. t->True. f->False. Both-> Include both in the results. <br/>
-sub->Mention the number of subtitles to download. *->All the ones found. [Currently not available]. <br/>
-lang->The language of the subtitle. <br/>
-ex->Extract the zipped file. t->True. f-> False. <br/>
-pos->Positive labeled subtitles. t->True. f->False. <br/>
-Last argument->This should be mentioned only in the end, or not at all. filename. Or a->Includes all the files in the current directory. <br/>
-help->To display the instructions. <br/>

Example:
python Lazy-Subscene.py -hi=t -dir=sub "Final.Fantasy.VII.Advent.Children.2005.720p.BrRip.x264.BOKUTOX.YIFY.mp4"

The script works by parsing the HTML output by searching the file name in Subscene.
So, it completely depends on Subscene's search logic.
