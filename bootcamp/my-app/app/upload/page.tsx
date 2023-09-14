// Uploading files
'use client';
import React from 'react'
import { CldUploadWidget, CldImage } from 'next-cloudinary'

const UploadPage = () => {
  return (
        <CldUploadWidget
            uploadPreset='xt7ekvnn'
            onUpload={(result, widget) => {
                console.log(result)
            }}>
            {({ open }) => 
                <button 
                    className='btn btn-primary'
                    onClick={() => open()}>Upload</button>}
        </CldUploadWidget>    
  )
}

export default UploadPage