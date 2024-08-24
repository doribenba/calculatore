class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v2/calculatore-1.0.1.tar.gz"
  sha256 "5cc6809ee28c6346daa6f3c8b76d44e07b7a3c69f869c818ddbf1ca3d4e0148a"

  def install
    bin.install "calculatore_universal" => "calculatore"
    man1.install "calculatore.1"
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
