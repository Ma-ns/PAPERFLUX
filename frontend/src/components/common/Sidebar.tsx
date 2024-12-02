"use client"
import page from '@/app/Relatorios/page';
import { useRouter } from 'next/navigation';
import React, { useState } from 'react'

const Sidebar: React.FC = () => {

  const route = useRouter();

  const [ selected, isSelected] = useState('Documentos');

  const PAGES_DATA = [
    {icon: '/images/icons/person.svg', title: 'Documentos', href: '/Documentos'},
    {icon: '/images/icons/person.svg', title: 'Colaboradores', href: '/Colaboradores'},
    {icon: '/images/icons/person.svg', title: 'Relatórios' , href: '/Relatorios'},
  ]

  const handlePageChange = (title: string, href: string) => {
    isSelected(title);
    route.push(href);
  }

  return (
    <div className='size-full bg-slate-50 px-8 py-4'>
      {/* LOGO */}
      <div className='h-[10%] w-full flex items-center justify-start'>
        <img src='/images/logo.png' alt='logo' className='w-40 object-contain' />
      </div>

      {/* USER CARD */}
      <div className='h-[18%] w-full flex items-center'>
        <div className='h-fit w-full py-2 flex items-center justify-between border-solid border-[1px] border-slate-300 rounded-lg'>
          <div className='w-[40%] h-full px-4 flex items-center'>
            <div className='size-[3.5rem] rounded-full overflow-clip border-solid border-[1px] border-slate-300'>
              <img src="/images/alunoUnijorge.jpg" alt="Foto usuário" className='w-full bg-cover ' />
            </div>
          </div>
          <div className='w-[60%] h-full flex flex-col justify-center items-start'>
            <h5 className='text-slate-950 font-bold text-base leading-5'>Maria Santana</h5>
            <h6 className='text-slate-700 text-sm font-medium leading-4'>Administrador</h6>
          </div>
        </div>
      </div>

      {/* NAVIGATION */}
      <div className='h-[62%] w-full'>
        <div>
          <button></button>
        </div>
        <div className='flex flex-col items-start justify-start gap-y-2'>
          {PAGES_DATA.map((page, pageIndex) => (
            <button key={pageIndex} onClick={() => handlePageChange(page.title, page.href)}
            className={'w-full h-fit flex items-center gap-x-1 group/button transition-all ' + 
            (selected === page.title ? 'bg-purple-100 px-4 py-3 rounded-lg' :
              'px-2 py-2 hover:bg-slate-200/80 rounded-lg'
            )}>
              <div>
                { page.title === 'Documentos' &&
                  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="34" viewBox="0 0 25 34" fill="none" className={'transition-all ' + (selected === page.title ? 'fill-purple-800 size-8' : 'fill-slate-700 group-hover/button:fill-purple-700 size-7')}>
                    <path d="M21.75 0.083374C22.5678 0.083374 23.352 0.408224 23.9303 0.986461C24.5085 1.5647 24.8334 2.34896 24.8334 3.16671V27.8334C24.8334 28.6511 24.5085 29.4354 23.9303 30.0136C23.352 30.5919 22.5678 30.9167 21.75 30.9167H3.25002C2.43227 30.9167 1.64801 30.5919 1.06977 30.0136C0.491537 29.4354 0.166687 28.6511 0.166687 27.8334V3.16671C0.166687 2.34896 0.491537 1.5647 1.06977 0.986461C1.64801 0.408224 2.43227 0.083374 3.25002 0.083374H21.75ZM12.5 17.0417H7.87502C7.46615 17.0417 7.07402 17.2041 6.7849 17.4933C6.49578 17.7824 6.33335 18.1745 6.33335 18.5834C6.33335 18.9922 6.49578 19.3844 6.7849 19.6735C7.07402 19.9626 7.46615 20.125 7.87502 20.125H12.5C12.9089 20.125 13.301 19.9626 13.5901 19.6735C13.8793 19.3844 14.0417 18.9922 14.0417 18.5834C14.0417 18.1745 13.8793 17.7824 13.5901 17.4933C13.301 17.2041 12.9089 17.0417 12.5 17.0417ZM17.125 9.33337H7.87502C7.48208 9.33381 7.10414 9.48427 6.81841 9.75401C6.53268 10.0238 6.36074 10.3924 6.33771 10.7847C6.31469 11.177 6.44231 11.5632 6.69451 11.8645C6.94671 12.1659 7.30446 12.3595 7.69465 12.4059L7.87502 12.4167H17.125C17.518 12.4163 17.8959 12.2658 18.1816 11.9961C18.4674 11.7263 18.6393 11.3577 18.6623 10.9654C18.6854 10.5731 18.5577 10.1869 18.3055 9.88555C18.0533 9.58423 17.6956 9.39058 17.3054 9.34417L17.125 9.33337Z"/>
                  </svg>
                }
                { page.title === 'Colaboradores' &&
                  <svg xmlns="http://www.w3.org/2000/svg" width="37" height="37" viewBox="0 0 37 37" fill="" className={'transition-all ' + (selected === page.title ? 'fill-purple-800 size-8' : 'fill-slate-700 group-hover/button:fill-purple-700 size-7')}>
                    <path d="M18.5 18.5C16.8042 18.5 15.3525 17.8961 14.1448 16.6885C12.9372 15.4809 12.3334 14.0291 12.3334 12.3333C12.3334 10.6375 12.9372 9.18572 14.1448 7.97808C15.3525 6.77045 16.8042 6.16663 18.5 6.16663C20.1959 6.16663 21.6476 6.77045 22.8552 7.97808C24.0629 9.18572 24.6667 10.6375 24.6667 12.3333C24.6667 14.0291 24.0629 15.4809 22.8552 16.6885C21.6476 17.8961 20.1959 18.5 18.5 18.5ZM6.16669 30.8333V26.5166C6.16669 25.643 6.39177 24.8403 6.84194 24.1085C7.2921 23.3768 7.88924 22.8177 8.63335 22.4312C10.2264 21.6347 11.8452 21.0375 13.4896 20.6398C15.134 20.242 16.8042 20.0427 18.5 20.0416C20.1959 20.0406 21.866 20.24 23.5104 20.6398C25.1549 21.0396 26.7736 21.6367 28.3667 22.4312C29.1118 22.8166 29.7095 23.3757 30.1596 24.1085C30.6098 24.8413 30.8344 25.644 30.8334 26.5166V30.8333H6.16669Z"/>
                  </svg>
                }
                { page.title === 'Relatórios' &&
                  <svg xmlns="http://www.w3.org/2000/svg" width="37" height="37" viewBox="0 0 37 37" fill="none" className={'transition-all ' + (selected === page.title ? 'fill-purple-800 size-8' : 'fill-slate-700 group-hover/button:fill-purple-700 size-7')}>
                    <path d="M27.75 4.625C28.9766 4.625 30.153 5.11228 31.0204 5.97963C31.8877 6.84699 32.375 8.02337 32.375 9.25V27.75C32.375 28.9766 31.8877 30.153 31.0204 31.0204C30.153 31.8877 28.9766 32.375 27.75 32.375H9.25C8.02337 32.375 6.84699 31.8877 5.97963 31.0204C5.11228 30.153 4.625 28.9766 4.625 27.75V9.25C4.625 8.02337 5.11228 6.84699 5.97963 5.97963C6.84699 5.11228 8.02337 4.625 9.25 4.625H27.75ZM24.215 14.3267C23.9259 14.0377 23.5338 13.8753 23.125 13.8753C22.7162 13.8753 22.3241 14.0377 22.035 14.3267L18.5 17.8602L16.5066 15.8684C16.2175 15.5794 15.8255 15.417 15.4167 15.417C15.0079 15.417 14.6158 15.5794 14.3267 15.8684L9.70171 20.4934C9.41269 20.7825 9.25033 21.1745 9.25033 21.5833C9.25033 21.9921 9.41269 22.3842 9.70171 22.6733L9.84662 22.8012C10.1432 23.0313 10.5136 23.1453 10.8883 23.1217C11.263 23.0982 11.6162 22.9387 11.8816 22.6733L15.4167 19.1398L17.41 21.1316L17.555 21.2596C17.8516 21.4897 18.222 21.6036 18.5966 21.5801C18.9713 21.5565 19.3245 21.3971 19.59 21.1316L23.125 17.5981L25.1184 19.59C25.4091 19.8708 25.7986 20.0262 26.2028 20.0227C26.607 20.0192 26.9937 19.857 27.2795 19.5712C27.5653 19.2853 27.7275 18.8987 27.731 18.4945C27.7345 18.0902 27.5791 17.7008 27.2983 17.41L24.215 14.3267Z"/>
                  </svg>
                }
              </div>
              <div className={'font-medium tracking-wide text-slate-700 transition-all ' + 
                (selected === page.title ? 'text-lg ' : 'text-base')}>
                {page.title}
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* LOG OUT */}
      <div className='h-[10%] w-full flex items-center py-2'>
        <button className='h-fit w-full bg-slate-400/80 hover:bg-slate-400 transition-all rounded-full'>
          <div>
            <h6 className='text-white font-medium py-2'>Sair</h6>
          </div>
        </button>
      </div>
    </div>
  )
}

export default Sidebar