<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';
  import RangeSlider from "svelte-range-slider-pips";

  let file: File | null = null;
  let gif: Blob | null = null;
  let loading = false;
  let uploadProgress = 0;
  let imageDistortionMinMax = [10,40];
  let fps = [24];
  
  const handleFileChange = (event: any) => {
    file = event.target.files[0];
    if (file) {
      (event.target as HTMLInputElement).style.backgroundImage = `url(${URL.createObjectURL(file)})`;
    }
  };
  
  const handleSubmit = async (event: any) => {
    if (!file) {
      return;
    }
  
    loading = true;
    (event.target as HTMLInputElement).style.backgroundImage = 'upload.jpeg';
    const formData = new FormData();
    formData.append('image', file);
    formData.append('name', "file");
    formData.append('fps', fps[0].toString());
    formData.append('min', imageDistortionMinMax[0].toString());
    formData.append('max', imageDistortionMinMax[1].toString());
  
    try {
      const response = await axios.post('http://192.168.1.249:8000/my-gif-maker/', formData, {
        responseType: 'blob',
        onUploadProgress: event => {
        uploadProgress = (event.loaded / event.total) * 100;
      }
      });
      gif = response.data;
    } catch (error) {
      console.error(error);
    }
    
    loading = false;
  };
  
  </script>
  
  <style>
    form {
      display: grid;
      flex-direction: column;
      align-items: center;
    }
  
    input[type="file"] {
      margin: 20px;
      border: dashed;
      cursor: pointer;
      background-image: url('./upload2.png');
      background-color: white;
      background-size: 100% 100%;
      height: 800px;
    }

    input[type="file"]::-webkit-file-upload-button {
      visibility: hidden;
      display: none;
    }

    progress {
      justify-self: center;
      width: 50%;
      height: 40px;
      border-radius: 50px;
      background-color: #ddd;
    }

    progress::-webkit-progress-bar {
      border-radius: 50px;
      background-color: #ddd;
    }

    progress::-webkit-progress-value {
      border-radius: 50px;
      background-color: #4caf50;
    }

    button {
      border-top: 100px;
      height: 50px;
      font-size: 25px;
    }

    .container {
      border: dashed;
      justify-content: center;
    }

    #gif {
      min-height: 400px;
      max-height: 700px;
    }

    #gif-div {
      display: flex;
      justify-content: center;
    }

    @media (max-width: 700px) {
      #parent {
        width: 500px;
      }
    }

  </style>

  <div id="parent">
    <form on:submit|preventDefault={handleSubmit}>
      {#if loading}
        <progress value={uploadProgress} max="100"><div>{uploadProgress}%</div></progress>
        {:else}
          <input id="fileInput" type="file" on:change={handleFileChange} class:loading={loading}/> 
          
          <div>
            <b>MIN {imageDistortionMinMax[0]} | MAX {imageDistortionMinMax[1]}</b>
            <RangeSlider id=small bind:values={imageDistortionMinMax} range float pips all="label" step={10} />
          </div>

          <div>
            <b>FPS: {fps[0]}</b>
            <RangeSlider id=small values:{24} bind:values={fps} range float pips max={30} step={1} />
          </div>

          <button id="submit" type="submit" disabled={loading}>Generate GIF</button>
      {/if}
    </form>
      {#if gif}
        <div id="gif-div">
          <img id="gif" src={URL.createObjectURL(gif)} alt="GIF" />
        </div>
      {/if}
  </div>
  