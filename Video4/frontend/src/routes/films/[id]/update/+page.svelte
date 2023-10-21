<script>
    import {FilmStore} from '../../../../film-store'
    import {goto} from '$app/navigation'
    import {onMount} from 'svelte'
    
    let name = '';
    let director = '';
    let description = ''
    let files;
    let showInvalidMessage = false;
    export let data;
    let id;

    let validFields = () => {
        return name.length > 4 && director.length > 4 && description.length > 10
    }

    let handleSubmit = () => {
        if (!validFields()) {
            showInvalidMessage = true;
            return
        }
        const endpoint = `http://localhost:8000/api/films/${id}/`
        let data = new FormData()
        data.append('name', name)
        data.append('director', director)
        data.append('description', description)

        if (files) {
            data.append('image', files[0])
        }
        
        fetch(endpoint, {method: 'PUT', body: data}).then(response => response.json()).then(data => {
            FilmStore.update(prev => {
                let updatedFilms = $FilmStore.slice()
                let index = updatedFilms.findIndex(film => film.id == data.id)
                updatedFilms[index] = data
                return updatedFilms
            })
        })
            

        goto('/films/')
    }

    onMount(async function() {
        id = data.id
        let film = {}
        if ($FilmStore.length) {
            film = $FilmStore.find(film => film.id == id)
        } else {
            const endpoint = `http://localhost:8000/api/films/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                film = await response.json()
            } else {
                film = null;
            }
        }
        ({name, director, description} = film)
    })

</script>


<div>

    <h2 class="my-4">Add a Film</h2>

    {#if showInvalidMessage }
        <h4 class="text-danger">Form data is not valid</h4>
    {/if }

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="name" bind:value={name}/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="director" bind:value={director}/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="description" bind:value={description}/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="file" bind:files/>
            </div>
        
            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>

</div>
