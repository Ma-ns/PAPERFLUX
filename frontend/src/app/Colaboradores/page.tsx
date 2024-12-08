"use client"
import React, { useEffect } from 'react'

const page:React.FC = () => {

  const [ users, setUsers ] = React.useState([])

  const fetchUserData = async() => {
    try {
      const response = await fetch('http://127.0.0.1:5000/user/all', {method: 'GET'})
      const data = await response.json();

      setUsers(data)

      return data
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchUserData()
  }, [])

  console.log(users)

  return (
    <section className='size-full flex flex-col items-start justify-between gap-y-4'>
      {/* REGISTER CARD */}
      <section className='w-full h-[30%]'>
        <div className='w-full h-fit pb-2'>
          <h1 className='text-3xl font-bold text-slate-950/80'>Colaboradores</h1>
        </div>
        <div className='z-0 w-full h-full bg-purple-100 rounded-lg py-2 flex items-center justify-between'>
          <div className='h-full w-[40%] px-8 flex flex-col items-start justify-center gap-y-2'>
            <h2 className='text-sm text-slate-800'>Novo funcionário?</h2>
            <h3 className='text-lg text-slate-950/80 font-medium mb-3 leading-5'>Cadastre-o no sistema para que tenha acesso ao PAPERFLUX!</h3>
            <button className='bg-purple-950 hover:bg-purple-950/90 transition-all text-white font-bold tracking-wide text-base w-full py-2 px-4 rounded-full'>Cadastrar</button>
          </div>
          <div className='h-full w-[40%] relative'>
            <div className='absolute right-8 bottom-8'>
              <svg xmlns="http://www.w3.org/2000/svg" width="251" height="192" viewBox="0 0 251 192" fill="none">
                <path d="M75 192C75 192 59 192 59 176C59 160 75 112 155 112C235 112 251 160 251 176C251 192 235 192 235 192H75ZM155 96C167.73 96 179.939 90.9429 188.941 81.9411C197.943 72.9394 203 60.7304 203 48C203 35.2696 197.943 23.0606 188.941 14.0589C179.939 5.05713 167.73 0 155 0C142.27 0 130.061 5.05713 121.059 14.0589C112.057 23.0606 107 35.2696 107 48C107 60.7304 112.057 72.9394 121.059 81.9411C130.061 90.9429 142.27 96 155 96Z" fill="#6D28D9"/>
                <path d="M77.05 52.6506L84.3048 71.5509C87.8323 80.7408 87.5442 90.9634 83.5038 99.97C79.4634 108.977 72.0018 116.029 62.7603 119.577C53.5188 123.124 43.2545 122.875 34.2255 118.885C25.1965 114.895 18.1423 107.491 14.6148 98.3011L1.31425 63.6506C0.672889 61.9797 0.725275 60.121 1.45989 58.4834C2.1945 56.8459 3.55117 55.5636 5.23144 54.9186C6.91171 54.2736 8.77794 54.3189 10.4196 55.0443C12.0612 55.7697 13.3438 57.116 13.9852 58.7869L22.4491 80.8372C22.7698 81.6727 23.4111 82.3458 24.2319 82.7085C25.0527 83.0713 25.9859 83.0939 26.826 82.7714C27.6661 82.4489 28.3445 81.8077 28.7118 80.989C29.0791 80.1702 29.1053 79.2408 28.7846 78.4054L15.4841 43.7548C14.8427 42.0839 14.8951 40.2253 15.6297 38.5877C16.3643 36.9501 17.721 35.6678 19.4013 35.0229C21.0815 34.3779 22.9478 34.4231 24.5894 35.1486C26.2311 35.874 27.5136 37.2202 28.155 38.8911L40.2464 70.3917C40.5671 71.2271 41.2083 71.9002 42.0292 72.2629C42.85 72.6257 43.7831 72.6483 44.6232 72.3258C45.4634 72.0033 46.1417 71.3622 46.509 70.5434C46.8763 69.7246 46.9025 68.7953 46.5818 67.9598L36.9087 42.7594C36.2674 41.0885 36.3198 39.2298 37.0544 37.5923C37.789 35.9547 39.1457 34.6724 40.8259 34.0274C42.5062 33.3825 44.3724 33.4277 46.0141 34.1531C47.6557 34.8786 48.9383 36.2248 49.5797 37.8957L61.7723 69.6601C57.6342 72.1093 54.493 75.9331 52.9038 80.4557C51.3146 84.9784 51.3795 89.9089 53.0872 94.3762C53.4079 95.2116 54.0492 95.8847 54.87 96.2475C55.6908 96.6102 56.6239 96.6328 57.4641 96.3103C58.3042 95.9878 58.9825 95.3467 59.3498 94.5279C59.7171 93.7091 59.7433 92.7798 59.4226 91.9443C58.1399 88.6025 58.2447 84.8852 59.7139 81.6101C61.1832 78.335 63.8965 75.7704 67.257 74.4804C68.0972 74.1579 68.7755 73.5168 69.1428 72.698C69.5101 71.8792 69.5363 70.9499 69.2156 70.1144L64.3791 57.5142C63.7377 55.8433 63.7901 53.9847 64.5247 52.3471C65.2593 50.7096 66.616 49.4273 68.2963 48.7823C69.9765 48.1373 71.8428 48.1825 73.4844 48.908C75.126 49.6334 76.4086 50.9797 77.05 52.6506Z" fill="#6D28D9"/>
              </svg>
            </div>
          </div>
        </div>
      </section>

      {/* MANAGEMENT SPACE */}
      <section className='w-full h-[60%]'>
        <div className='w-full h-fit flex items-end justify-between'>
          <h2 className='text-xl font-bold text-slate-900/80'>Recentes</h2>
          <div className='w-fit h-fit'>
            <div className='relative w-[20rem] group/search border-solid border-b-[1px] border-slate-300 h-fit bg-slate-50'>
              <div className='absolute z-10 pointer-events-none size-full flex items-center justify-end px-4 py-2'>
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" className='size-6 fill-slate-800/80'>
                  <g  fillRule="evenodd" clipRule="evenodd"><path d="M10.5 5.5a5 5 0 1 0 0 10a5 5 0 0 0 0-10m-6.5 5a6.5 6.5 0 1 1 13 0a6.5 6.5 0 0 1-13 0"/><path d="M14.47 14.47a.75.75 0 0 1 1.06 0l4 4a.75.75 0 1 1-1.06 1.06l-4-4a.75.75 0 0 1 0-1.06"/></g>
                </svg>
              </div>
              <input 
              className='relative z-0 size-full appearance-none outline-none bg-transparent px-4 py-2 text-slate-800/80'
              placeholder='Pesquisar...'>
              </input>
            </div>
          </div>
        </div>
        
        <div className='w-full h-full flex flex-col mt-4'>
          <div className='w-full h-fit flex items-center justify-between mb-2'>
            <h3 className='text-sm font-semibold text-slate-800/60 w-[40%] flex items-center justify-start'>Nome e Cargo</h3>
            <h3 className='text-sm font-semibold text-slate-800/60 w-[40%] flex items-center justify-start'>Email</h3>
            <h3 className='text-sm font-semibold text-slate-800/60  w-[20%] flex items-center justify-start'>Ações</h3>
          </div>

          {/* Tabela */}
          <div className='w-full h-full flex flex-col items-start justify-start gap-y-2'>
            {users.map((user, userIndex) => (
              <div key={userIndex} className='w-full h-fit py-2 px-4 border-solid border-[2px] border-purple-800/15 rounded-lg flex items-center justify-between'>
                <div className='w-[40%] h-fit flex items-center justify-start gap-x-4'>
                  <img src="/uploads/test.jpg" alt="" className='size-16 object-cover object-center rounded-full'></img>
                  <div className='size-fit'>
                    <h4 className='text-base font-medium text-slate-800/80'>Usuário</h4>
                    <h5 className='text-xs font-regular text-slate-800/60'>Cargo</h5>
                  </div>
                </div>

                <div className='w-[40%] h-full flex items-center justify-start'>
                  <h5 className='w-full h-fit text-left font-regular text-slate-800/80'>Email</h5>
                </div>
                <div className='w-[20%] h-full flex items-center justify-start gap-x-2'>
                  <button className='size-12 rounded-lg border-solid border-[2px] border-purple-800/30 bg-purple-800/5 
                  hover:bg-purple-800/10 transition-all'>
                    <div className='size-full flex items-center justify-center'>
                      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="17" viewBox="0 0 22 17" fill="none" className='size-6'>
                        <path fillRule="evenodd" clipRule="evenodd" d="M0.068479 8.136C1.80248 3.694 5.88348 0.5 10.9995 0.5C16.1155 0.5 20.1965 3.694 21.9315 8.136C22.0229 8.37005 22.0229 8.62995 21.9315 8.864C20.1965 13.306 16.1155 16.5 10.9995 16.5C5.88348 16.5 1.80248 13.306 0.068479 8.864C-0.0229891 8.62995 -0.0229891 8.37005 0.068479 8.136ZM10.9995 11.5C11.7951 11.5 12.5582 11.1839 13.1208 10.6213C13.6834 10.0587 13.9995 9.29565 13.9995 8.5C13.9995 7.70435 13.6834 6.94129 13.1208 6.37868C12.5582 5.81607 11.7951 5.5 10.9995 5.5C10.2038 5.5 9.44077 5.81607 8.87816 6.37868C8.31555 6.94129 7.99948 7.70435 7.99948 8.5C7.99948 9.29565 8.31555 10.0587 8.87816 10.6213C9.44077 11.1839 10.2038 11.5 10.9995 11.5Z" fill="#3B0764"/>
                      </svg>
                    </div>
                  </button>
                  <button className='size-12 rounded-lg border-solid border-[2px] border-purple-800/30 bg-purple-800/5 
                  hover:bg-purple-800/10 transition-all'>
                    <div className='size-full flex items-center justify-center'>
                      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="19" viewBox="0 0 18 19" fill="none" className='size-6'>
                        <path d="M9.9144 4.34343L14.1564 8.58543L4.2564 18.4854H0.0144043V14.2424L9.9144 4.34343ZM11.3284 2.92843L13.4494 0.807435C13.6369 0.619964 13.8912 0.514648 14.1564 0.514648C14.4216 0.514648 14.6759 0.619964 14.8634 0.807435L17.6924 3.63543C17.7854 3.72831 17.8591 3.8386 17.9095 3.95999C17.9598 4.08139 17.9857 4.21152 17.9857 4.34293C17.9857 4.47435 17.9598 4.60448 17.9095 4.72588C17.8591 4.84727 17.7854 4.95756 17.6924 5.05043L15.5704 7.17143L11.3284 2.92843Z" fill="#3B0764"/>
                      </svg>
                    </div>
                  </button>
                  <button className='size-12 rounded-lg border-solid border-[2px] border-purple-800/30 bg-purple-800/5 
                  hover:bg-purple-800/10 transition-all'>
                    <div className='size-full flex items-center justify-center'>
                      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="21" viewBox="0 0 18 21" fill="none" className='size-6'>
                        <path d="M17.25 3.75H13.5V3C13.5 2.40326 13.2629 1.83097 12.841 1.40901C12.419 0.987053 11.8467 0.75 11.25 0.75H6.75C6.15326 0.75 5.58097 0.987053 5.15901 1.40901C4.73705 1.83097 4.5 2.40326 4.5 3V3.75H0.75C0.551088 3.75 0.360322 3.82902 0.21967 3.96967C0.0790178 4.11032 0 4.30109 0 4.5C0 4.69891 0.0790178 4.88968 0.21967 5.03033C0.360322 5.17098 0.551088 5.25 0.75 5.25H1.5V18.75C1.5 19.1478 1.65804 19.5294 1.93934 19.8107C2.22064 20.092 2.60218 20.25 3 20.25H15C15.3978 20.25 15.7794 20.092 16.0607 19.8107C16.342 19.5294 16.5 19.1478 16.5 18.75V5.25H17.25C17.4489 5.25 17.6397 5.17098 17.7803 5.03033C17.921 4.88968 18 4.69891 18 4.5C18 4.30109 17.921 4.11032 17.7803 3.96967C17.6397 3.82902 17.4489 3.75 17.25 3.75ZM7.5 15C7.5 15.1989 7.42098 15.3897 7.28033 15.5303C7.13968 15.671 6.94891 15.75 6.75 15.75C6.55109 15.75 6.36032 15.671 6.21967 15.5303C6.07902 15.3897 6 15.1989 6 15V9C6 8.80109 6.07902 8.61032 6.21967 8.46967C6.36032 8.32902 6.55109 8.25 6.75 8.25C6.94891 8.25 7.13968 8.32902 7.28033 8.46967C7.42098 8.61032 7.5 8.80109 7.5 9V15ZM12 15C12 15.1989 11.921 15.3897 11.7803 15.5303C11.6397 15.671 11.4489 15.75 11.25 15.75C11.0511 15.75 10.8603 15.671 10.7197 15.5303C10.579 15.3897 10.5 15.1989 10.5 15V9C10.5 8.80109 10.579 8.61032 10.7197 8.46967C10.8603 8.32902 11.0511 8.25 11.25 8.25C11.4489 8.25 11.6397 8.32902 11.7803 8.46967C11.921 8.61032 12 8.80109 12 9V15ZM12 3.75H6V3C6 2.80109 6.07902 2.61032 6.21967 2.46967C6.36032 2.32902 6.55109 2.25 6.75 2.25H11.25C11.4489 2.25 11.6397 2.32902 11.7803 2.46967C11.921 2.61032 12 2.80109 12 3V3.75Z" fill="#3B0764"/>
                      </svg>
                    </div>
                  </button>

                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </section>
  )
}

export default page