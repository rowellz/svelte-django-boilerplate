<script lang="ts">
  let stream;

  let audio: MediaStream | null = null;
  let mediaRecorder: MediaRecorder | null = null;
  let chunks: Blob[] = [];
  let audioUrl: string | null = null;
  let audioElement: HTMLAudioElement | null = null;
  const audioCtx = new AudioContext();

  // let mediaRecorder;

  let recordButton: HTMLButtonElement;
  // let chunks = [];

  let clips: any[] = [];

  function onStop(e: Event) {
    console.log("recorder stopped");
	console.log(chunks);
	
    const blob = new Blob(chunks, { type: "audio/wav" });
    chunks = [];
    const audioURL = window.URL.createObjectURL(blob);
    console.log(audioURL);

    clips = [
      ...clips,
      {
        src: audioURL,
      },
    ];
    console.log(clips);
  }

  async function setup() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      console.log("getUserMedia supported.");
      stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);

	  mediaRecorder.ondataavailable = (e) => {
		  console.log(e.data);
		  
		  chunks.push(e.data);
	  }

      mediaRecorder.onstop = onStop;
    }
  }

  setup();

  function record() {
    if (mediaRecorder) { 
      console.log("recorder started");
      mediaRecorder.start();
      recordButton.style.background = "red";
      recordButton.style.color = "black";
   }
  }

  function stop() {
    if (mediaRecorder) { 
    mediaRecorder.stop();
    console.log(mediaRecorder.state);
    console.log("recorder stopped");
    recordButton.style.background = "";
    recordButton.style.color = "";
    }
  }

  function upload() {
    if (clips) { 

    }
  }
</script>

<div class="wrapper">
  <header>
    <h1>Web dictaphone</h1>
  </header>

  <section class="main-controls">
    <canvas class="visualizer" height="60px" />
    <div id="buttons">
      <button class="record" on:click={record} bind:this={recordButton}
        >Record</button
      >
      <button class="stop" on:click={stop}>Stop</button>
    </div>
  </section>

  <section class="sound-clips">
    {#each clips as clip}
      <article class="clip">
        <p>clip</p>
        <audio src={clip.src} controls/>
        <button on:click={stop}>Upload</button>
        <button>Delete</button>
        Download <a href={clip.src}>test</a>
      </article>
    {/each}
  </section>
</div>

<label for="toggle">❔</label>
<input type="checkbox" id="toggle" />
<aside>
  <h2>Information</h2>

  <p>
    Web dictaphone is built using <a
      href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator.getUserMedia"
      >getUserMedia</a
    >
    and the
    <a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder_API"
      >MediaRecorder API</a
    >, which provides an easier way to capture Media streams.
  </p>

</aside>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html,
  body {
    height: 100%;
  }

  body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 0.8rem;
  }

  .wrapper {
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  h1,
  h2 {
    font-size: 2rem;
    text-align: center;
    font-weight: normal;
    padding: 0.5rem 0 0 0;
  }

  .main-controls {
    padding: 0.5rem 0;
  }

  canvas {
    display: block;
    margin-bottom: 0.5rem;
  }

  #buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  #buttons button {
    font-size: 1rem;
    padding: 1rem;
    width: calc(50% - 0.25rem);
  }

  button {
    font-size: 1rem;
    background: #0088cc;
    text-align: center;
    color: white;
    border: none;
    transition: all 0.2s;
    padding: 0.5rem;
  }

  button:hover,
  button:focus {
    box-shadow: inset 0px 0px 10px rgba(255, 255, 255, 1);
    background: #0ae;
  }

  button:active {
    box-shadow: inset 0px 0px 20px rgba(0, 0, 0, 0.5);
    transform: translateY(2px);
  }

  /* Make the clips use as much space as possible, and
 * also show a scrollbar when there are too many clips to show
 * in the available space */
  .sound-clips {
    flex: 1;
    overflow: auto;
  }

  section,
  article {
    display: block;
  }

  .clip {
    padding-bottom: 1rem;
  }

  audio {
    width: 100%;
    display: block;
    margin: 1rem auto 0.5rem;
  }

  .clip p {
    display: inline-block;
    font-size: 1rem;
  }

  .clip button {
    font-size: 1rem;
    float: right;
  }

  button.delete {
    background: #f00;
    padding: 0.5rem 0.75rem;
    font-size: 0.8rem;
  }

  /* Checkbox hack to control information box display */

  label {
    font-size: 3rem;
    position: absolute;
    top: 2px;
    right: 3px;
    z-index: 5;
    cursor: pointer;
    background-color: black;
    border-radius: 10px;
  }

  input[type="checkbox"] {
    position: absolute;
    top: -100px;
  }

  aside {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform: translateX(100%);
    transition: 0.3s all ease-out;
    background-color: #efefef;
    padding: 1rem;
  }

  aside p {
    font-size: 1.2rem;
    margin: 0.5rem 0;
  }

  aside a {
    color: #666;
  }

  /* Toggled State of information box */
  input[type="checkbox"]:checked ~ aside {
    transform: translateX(0);
  }

  /* Cursor when clip name is clicked over */

  .clip p {
    cursor: pointer;
  }

  /* Adjustments for wider screens */
  @media all and (min-width: 800px) {
    /* Don't take all the space as readability is lost when line length
     goes past a certain size */
    .wrapper {
      width: 90%;
      max-width: 1000px;
      margin: 0 auto;
    }
  }
</style>