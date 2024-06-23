<script lang="ts">
	import axios from 'axios';
  
	let textInput: string = '';
	let responseText: string | null = null;
  
	async function handleSubmit() {
	  try {
		const formData = new FormData();
    	formData.append('text', textInput);
		const response = await axios.post('api/open-ai/', formData);
		responseText = response.data.replace(/<br\s*[\/]?>/gi, "\n");
		// responseText = response.data;
		console.log(responseText)
	  } catch (error) {
		console.error(error);
	  }
	}
  </script>
<head>
	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		.recipe-container {
			max-width: 800px;
			margin: 0 auto;
			padding: 20px;
			box-sizing: border-box;
		}
		.recipe-title {
			text-align: center;
			font-size: 32px;
			font-weight: bold;
			margin-bottom: 20px;
			color: #333;
		}
		.ingredients, .instructions {
			width: 100%;
			border-collapse: collapse;
			margin-bottom: 20px;
		}
		.ingredients th, .instructions th {
			background-color: #333;
			color: #fff;
			font-size: 16px;
			padding: 10px;
			text-align: left;
		}
		.ingredients td, .instructions td {
			padding: 10px;
			font-size: 14px;
			border-bottom: 1px solid #ccc;
		}
		.ingredients td:first-child {
			font-weight: bold;
			width: 30%;
		}
		.instructions ol {
			padding-left: 20px;
			margin: 0;
		}
		.instructions ol li {
			margin-bottom: 10px;
			font-size: 14px;
		}
		#text-input {
			min-width: 200px;
		}
		pre {
  			max-width: 400px;
		}

	</style>
</head>
<body>
	<div class="recipe-container">
		<h1 class="recipe-title">Make Axios Request to Django API</h1>
		  <form on:submit|preventDefault={handleSubmit}>
			<label for="text-input">What would you like to find a recipe for?:</label>
			<input type="text" id="text-input" bind:value={textInput} />
			<button type="submit">Submit</button>
		  </form>
		  {#if responseText}
			<pre>{responseText}</pre>
		  {/if}
	</div> 
</body>

  

  