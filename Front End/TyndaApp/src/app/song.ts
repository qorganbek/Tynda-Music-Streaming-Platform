export interface Song {
  id: string,

  title: string,

  image: string,

  audio: string,

  is_top: boolean,

  created_at: string,

  updated_at: string,

  category: string,

  artist: string[]
}


export let SONGS: Song[] = [
  {
    "id": "c5d9bf1c-5019-491f-ae1c-9b945f60d3b1",
    "title": "Cocaina",
    "image": "http://localhost:8000/media/images/2023/04/07/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2023-04-02_191639.png",
    "audio": "http://localhost:8000/media/audios/2023/04/07/ss1.mp3",
    "is_top": true,
    "created_at": "2023-04-07T13:44:35.700218Z",
    "updated_at": "2023-04-07T13:44:35.700218Z",
    "category": "c4fd088c-45b3-4018-8d45-0f49853c979f",
    "artist": [
      "219d3bb5-1a2f-4b66-a31c-26bc4df4c9da"
    ]
  },
  {
    "id": "d049607f-5585-4fa4-90d0-4ef196f29042",
    "title": "Izdeme",
    "image": "http://localhost:8000/media/images/2023/04/07/CV_example.png",
    "audio": "http://localhost:8000/media/audios/2023/04/07/%D0%A2%D3%A9%D1%80%D0%B5%D2%93%D0%B0%D0%BB%D0%B8_%D0%A2%D3%A9%D1%80%D0%B5%D3%99%D0%BB%D1%96_-_%D0%86%D0%B7%D0%B4%D0%B5%D0%BC%D0%B5.mp3",
    "is_top": true,
    "created_at": "2023-04-07T13:43:12.212164Z",
    "updated_at": "2023-04-07T13:43:12.212164Z",
    "category": "71ce5f08-43a7-4ba4-9dd0-5891e832bec6",
    "artist": [
      "7f648d49-562e-4d48-800c-9747b2e8e471"
    ]
  }
]
