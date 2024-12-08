"use client"
import React, { useEffect } from 'react'

export interface FolderI {
  id: number
  name: string
  description: string
  private: string
}

export interface DocumentI{
  created_at: string
  description: string
  document_id: number
  extension: string
  extracted_data: JSON
  folder_id: number
  modified_at: string
  modified_data: string
  name: string
  page_count: number
  path: string
}

const page:React.FC = () => {
  const [folders, setFolders] = React.useState<FolderI[]>([])
  const [documents, setDocuments] = React.useState<DocumentI[]>([])

  const fetchFolder = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/folder/all', {method: 'GET'})
      const data = await response.json();

      setFolders(data.folders)

      return data
    } catch (error) {
      console.log(error)
    }
  }

  const fetchDocuments = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/document/all', {method: 'GET'})
      const data = await response.json();

      setDocuments(data)

      return data
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchFolder()
    fetchDocuments()
  },[])
console.log(documents)
  return (
    <section className='size-full flex flex-col items-start justify-between gap-y-4'>
      {/* REGISTER CARD */}
      <section className='w-full h-[30%]'>
        <div className='w-full h-fit pb-2'>
          <h1 className='text-3xl font-bold text-slate-950/80'>Documentos</h1>
        </div>
        <div className='z-0 w-full h-full bg-purple-100 rounded-lg py-2 flex items-center justify-between'>
          <div className='h-full w-[40%] px-8 flex flex-col items-start justify-center gap-y-2'>
            <h2 className='text-sm text-slate-800'>Novo documento?</h2>
            <h3 className='text-lg text-slate-950/80 font-medium mb-3 leading-5'>Cadastre-o no Paperflux para digitalizar, extrair seus dados e o assinar digitalmente!</h3>
            <button className='bg-purple-950 hover:bg-purple-950/90 transition-all text-white font-bold tracking-wide text-base w-full py-2 px-4 rounded-full'>Cadastrar</button>
          </div>
          <div className='h-full w-[40%] relative'>
            <div className='absolute right-8 -top-16'>
              <svg width="269" height="280" viewBox="0 0 269 280" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="152.995" y="117.003" width="117.452" height="146.318" rx="5" transform="rotate(9.00591 152.995 117.003)" className='fill-purple-400'/>
                <rect x="163.007" y="141.265" width="90.08" height="8.21171" rx="4.10586" transform="rotate(9.00591 163.007 141.265)"  className='fill-purple-700'/>
                <rect x="161.293" y="152.079" width="90.08" height="8.21171" rx="4.10586" transform="rotate(9.00591 161.293 152.079)" className='fill-purple-700'/>
                <rect x="157.593" y="175.427" width="90.08" height="4.23028" rx="2.11514" transform="rotate(9.00591 157.593 175.427)" className='fill-purple-700'/>
                <rect x="156.23" y="184.029" width="47.7772" height="4.23028" rx="2.11514" transform="rotate(9.00591 156.23 184.029)" className='fill-purple-700'/>
                <rect x="159.579" y="162.893" width="90.08" height="8.21171" rx="4.10586" transform="rotate(9.00591 159.579 162.893)" className='fill-purple-700'/>
                <rect x="70.6709" y="1.70308" width="178.399" height="221.26" rx="7" transform="rotate(9.30012 70.6709 1.70308)" className='fill-purple-400' stroke="white" strokeWidth="4"/>
                <rect x="87.0022" y="40.1011" width="133.755" height="12.1932" rx="5" transform="rotate(9.30012 87.0022 40.1011)" className='fill-purple-700'/>
                <rect x="84.3749" y="56.1449" width="133.755" height="12.1932" rx="5" transform="rotate(9.30012 84.3749 56.1449)" className='fill-purple-700'/>
                <rect x="78.7023" y="90.7849" width="133.755" height="6.28132" rx="3.14066" transform="rotate(9.30012 78.7023 90.7849)" className='fill-purple-700'/>
                <rect x="76.6123" y="103.547" width="70.942" height="6.28132" rx="3.14066" transform="rotate(9.30012 76.6123 103.547)" className='fill-purple-700'/>
                <rect x="81.7477" y="72.1886" width="133.755" height="12.1932" rx="5" transform="rotate(9.30012 81.7477 72.1886)" className='fill-purple-700'/>
                <rect x="0.6545" y="168.716" width="98.3003" height="90.3475" rx="12" transform="rotate(-11.0227 0.6545 168.716)" className='fill-purple-400' stroke="white" strokeWidth="4"/>
                <circle cx="33.1566" cy="190.465" r="7.63967" className='fill-purple-700'/>
                <path d="M71.634 223.457L52.4957 203.535C49.59 200.511 44.5039 201.721 43.272 205.73L35.1574 232.137C33.908 236.203 37.5497 240.088 41.688 239.103L68.9408 232.618C73.0791 231.634 74.5809 226.525 71.634 223.457Z" className='fill-purple-700'/>
                <path d="M99.2404 216.544L73.337 189.579C70.4314 186.555 65.3453 187.765 64.1133 191.774L53.1305 227.515C51.881 231.581 55.5228 235.466 59.661 234.481L96.5472 225.704C100.685 224.72 102.187 219.611 99.2404 216.544Z" className='fill-purple-700'/>
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

        <div className='size-full my-4 pb-2 overflow-y-auto overflow-x-hidden '>
          <div className='h-fit w-full pr-2'>
            <h3 className='text-sm font-bold text-slate-800/60 mb-2'>Pastas</h3>
            <div className='w-full h-fit flex items-center justify-start gap-x-4'>
              {folders.map((folder, folderIndex) => (
                <button key={folderIndex} className='h-fit w-[12rem] py-3 px-4 group/folder bg-purple-800/10 hover:bg-purple-800/15 transition-all rounded-lg flex items-center justify-start gap-x-2'>
                  <div className='size-fit'>
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="24" viewBox="0 0 30 24" fill="none" className='size-6 fill-purple-800 group-hover/folder:fill-purple-900 transition-all'>
                      <path d="M12 0H3C1.35 0 0.015 1.35 0.015 3L0 21C0 22.65 1.35 24 3 24H27C28.65 24 30 22.65 30 21V6C30 4.35 28.65 3 27 3H15L12 0Z" fillOpacity="0.6"/>
                    </svg>
                  </div>
                  <div className='w-full text-base font-medium text-slate-800/80 group-hover/folder:text-slate-800/90 transition-all'>
                    {folder.name}
                  </div>
                </button>
              ))}
            </div>
          </div>
          <div className='h-full w-full py-4 pr-2'>
            <h3 className='text-sm font-bold text-slate-800/60'>Documentos</h3>
            <div className='w-full h-full flex items-start justify-start flex-wrap gap-2'>
              {documents.map((document, documentIndex) => (
                <button key={documentIndex} 
                className='px-2 py-2 flex flex-col grow max-w-[16rem] h-[12rem] border-solid border-[2px] border-purple-800/15 rounded-lg group
                hover:bg-purple-800/3 hover:border-purple-800/30 transition-all'>
                  <div className='w-full h-[60%]'>
                    <img src={`${document.path}`} alt="" className='object-cover object-center size-full rounded-lg'></img>
                  </div>
                  <div className='w-full h-[40%] px-1'>
                    <h4 className='mt-2 text-left text-base font-medium text-slate-800/80 group-hover:text-slate-800 transition-all'>{document.name}</h4>
                    <p className='text-xs text-left text-slate-800/60 group-hover:text-slate-800/80 transition-all line-clamp-2 text-ellipsis'>{document.description}</p>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>
      </section>
    </section>
  )
}

export default page