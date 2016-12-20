<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Home extends CI_Controller {

	function __construct()
	{
		parent::__construct();
		$this->load->helper('url');
		//$this->load->database(); // Sayfada database ye  eri�memizi sa�lar
		$this->load->library('session');
	}
	
	public function index()
	{
		//$data['title']="Anasayfa";

		//$query=$this->db->get("settings");
		//$data["veri"]=$query->result();

		//$query=$this->db->query("select * from paylasimlar order by id desc limit 5");
		//$data["veri"]=$query->result();


		/*if ($this->session->userdata('logged_in'))
		{
			$session_data = $this->session->userdata('logged_in');
			$data['adsoy'] = $session_data['adsoy'];
			$data['kullaniciadi'] = $session_data['kullaniciadi'];
			$data['id'] = $session_data['id'];
			$data['email'] = $session_data['email'];
		}		
		*/

		$this->load->view('header');			
		
		$this->load->view('content_login');
		
		$this->load->view('footer');
	}
	
	public function login()
	{
		//$data['title']="Anasayfa";

		//$query=$this->db->get("settings");
		//$data["veri"]=$query->result();

		//$query=$this->db->query("select * from paylasimlar order by id desc limit 5");
		//$data["veri"]=$query->result();


		/*if ($this->session->userdata('logged_in'))
		{
			$session_data = $this->session->userdata('logged_in');
			$data['adsoy'] = $session_data['adsoy'];
			$data['kullaniciadi'] = $session_data['kullaniciadi'];
			$data['id'] = $session_data['id'];
			$data['email'] = $session_data['email'];
		}		
		*/

		$this->load->view('header');			
		
		$this->load->view('content_login');
		
		$this->load->view('footer');
	}
	
	public function paylasim_ekle()
	{  
		$this->load->model('Paylasim_model'); // Kay�t i�leminin yap�laca�� model
		// Kay�t formundandan bilgileri al
		// form nesnelerinden al�nan veriler tablo alanlar� ile e�le�tiriliyor
		$data=array(
		'baslik' => $this->input->post('baslik'),
		'title' => $this->input->post('title'),
		'description' => $this->input->post('description'),
		'name' => $this->input->post('name'),
		'keywords' => $this->input->post('keywords'),
		'icerik' => $this->input->post('icerik')
		);
		
		// Data dizisine y�klenen verileri models teki ilgili fonksiyona g�nderme
		$this->Paylasim_model->insert_paylasim($data); // ekleme fonk. datalar� g�nder
		
		redirect(base_url()."index.php/admin/paylasimlar");		
	
	}
	 public function paylasim_sil($id)
	{ 
		$this->load->model('Paylasim_model'); // Kay�t i�leminin yap�laca�� model
		$this->Paylasim_model->delete_paylasim($id); // Parametre ile al�nan ID yi silme fonksiyonuna g�nder
		redirect(base_url()."index.php/admin/paylasimlar");
	}
	 public function paylasim_duzenle($id)
	{
		$this->load->helper('form');
		
	if ($this->session->userdata('logged_in'))
		{
			$session_data = $this->session->userdata('logged_in');
			$data['adsoy'] = $session_data['adsoy'];
			$data['kullaniciadi'] = $session_data['kullaniciadi'];
			$data['id'] = $session_data['id'];
			$data['email'] = $session_data['email'];
			
		$this->load->view('admin/header',$data);
		$this->load->view('admin/sidebar',$data);
		$query=$this->db->query("select * from paylasimlar where Id=".$id);
		$data["veri"]=$query->result();	
		$this->load->view('admin/content_paylasim_duzenle',$data);
		$this->load->view('admin/footer');
		}	
		else{
			redirect(base_url()."index.php/admin/giris");
		}
		
		
	}
	
	public function paylasim_guncelle($id) // D�zenleme formundan gelen verileri g�ncelleme
	{  
		$this->load->model('Paylasim_model'); // Kay�t i�leminin yap�laca�� model
		
		
		// form nesnelerinden al�nan veriler tablo alanlar� ile e�le�tiriliyor
		$data=array(
		'baslik' => $this->input->post('baslik'),
		'title' => $this->input->post('title'),
		'keywords' => $this->input->post('keywords'),
		'description' => $this->input->post('description'),
		'name' => $this->input->post('name'),
		'icerik' => $this->input->post('icerik')
		);
		
		// Data dizisine y�klenen verileri models teki ilgili fonksiyona g�nderme
		$this->Paylasim_model->update_paylasim($data,$id); //  fonksiypnua datalar� id ile  g�nder
		
		redirect(base_url()."index.php/admin/paylasimlar");
	
	}
	
}	
